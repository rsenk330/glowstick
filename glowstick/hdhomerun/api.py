import six

from ctypes import byref, c_char_p
from ipaddress import IPv4Address
from types import MethodType

from . import lib
from .constants import HDHOMERUN_DEVICE_ID_WILDCARD, HDHOMERUN_DEVICE_TYPE_TUNER, HDHOMERUN_DEVICE_TYPE_WILDCARD
from .exceptions import DeviceError, HomeRunError, NoDeviceError
from .structs import hdhomerun_discover_device_t


class HDHomeRunLibrary:
    """Calls any known functions from libhdhomerun.

        lib = HDHomeRunLibrary()
        lib.hdhomerun_device_get_device_ip(hd)

    """

    def __getattr__(self, name):
        attr = getattr(lib, name)
        if attr:
            if type(attr) == MethodType:
                return lambda *args, **kwargs: attr(*args, **kwargs)
            else:
                return attr

        return super().__getattr(name)


HDHOMERUN_LIB = HDHomeRunLibrary()


class Tuner:
    def __init__(self, device, tuner_num):
        self._device = device
        self.tuner_num = tuner_num

    def __repr__(self):
        return "<{} {}>".format(self.__class__.__name__, self.tuner_num)


class Device:
    def __init__(self, device_id=0, device_ip=0):
        if device_id == 0 and device_ip == 0:
            raise ValueError("You must provide either a device_id or device_ip")

        if device_ip != 0:
            device_ip = IPv4Address(device_ip)
            if device_ip.is_multicast:
                raise ValueError("Cannot use multicast ip address for device operations")

        if isinstance(device_id, six.string_types):
            device_id = int(device_id, 16)
        device_id_str = "{:8X}".format(device_id).encode("utf-8")

        discover_hd = hdhomerun_discover_device_t()
        found = HDHOMERUN_LIB.hdhomerun_discover_find_devices_custom(int(device_ip), HDHOMERUN_DEVICE_TYPE_WILDCARD, int(device_id), discover_hd, 1)
        if found <= 0:
            raise NoDeviceError("No device found: {}".format(device_id_str))

        hd = HDHOMERUN_LIB.hdhomerun_device_create_from_str(device_id_str, None)
        if not hd:
            raise DeviceError("Invalid device id {}.".format(device_id_str))

        # Device ID check
        device_id_requested = HDHOMERUN_LIB.hdhomerun_device_get_device_id_requested(hd)
        if not HDHOMERUN_LIB.hdhomerun_discover_validate_device_id(device_id_requested):
            raise DeviceError("Invalid device id: {}".format(device_id_requested))

        # Connect to device and check model
        model = HDHOMERUN_LIB.hdhomerun_device_get_model_str(hd)
        if not model:
            HDHOMERUN_LIB.hdhomerun_device_destroy(hd)
            raise DeviceError("Unable to connect to device")

        self._id = device_id_requested
        self._ip = HDHOMERUN_LIB.hdhomerun_device_get_device_ip(hd)
        self._hd = hd
        self._discover_hd = discover_hd
        self.tuners = tuple(Tuner(hd, t + 1) for t in range(discover_hd.tuner_count))

    def __repr__(self):
        return "<{} {} at {}>".format(self.__class__.__name__, self.id, self.ip)

    @property
    def id(self):
        return "{:8X}".format(self._id)

    @property
    def ip(self):
        return str(IPv4Address(self._discover_hd.ip_addr))

    @property
    def copyright(self):
        return self.get(b"/sys/copyright")

    @property
    def features(self):
        return self.get(b"/sys/features")

    @property
    def hwmodel(self):
        return self.get(b"/sys/hwmodel")

    @property
    def model(self):
        return self.get(b"/sys/model")

    @property
    def tuner_count(self):
        return self._discover_hd.tuner_count

    @property
    def version(self):
        return self.get(b"/sys/version")

    def get_tuner(self):
        return HDHOMERUN_LIB.hdhomerun_device_get_tuner(self._hd)

    def get_lineup(self):
        location = c_char_p()
        HDHOMERUN_LIB.hdhomerun_device_get_lineup_location(self._hd, byref(location))

        return location.value.decode("utf-8")

    def get(self, key):
        ret_value = c_char_p()
        ret_error = c_char_p()
        HDHOMERUN_LIB.hdhomerun_device_get_var(self._hd, key, ret_value, ret_error)

        if ret_error.value:
            raise DeviceError(ret_error.value.decode("utf-8"))

        return ret_value.value.decode("utf-8")


def get_devices():
    """Gets a list of devices on the network.

    :returns: A list of hdhomerun devices

    """
    results = (HDHOMERUN_LIB.hdhomerun_discover_device_t * 64)()
    devices_found = HDHOMERUN_LIB.hdhomerun_discover_find_devices_custom(
        0, HDHOMERUN_DEVICE_TYPE_TUNER, HDHOMERUN_DEVICE_ID_WILDCARD, results, 64
    )

    if devices_found < 0:
        raise HomeRunError("Error discovering devices")
    elif devices_found == 0:
        raise NoDeviceError("No devices could be found")

    return [Device(device_id=d.device_id) for i, d in enumerate(results) if i < devices_found]
