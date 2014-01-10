from ctypes import c_char_p, pointer
from types import MethodType

from . import utils
from . import lib
from .constants import HDHOMERUN_DEVICE_ID_WILDCARD, HDHOMERUN_DEVICE_TYPE_TUNER
from .exceptions import DeviceError, HomeRunError, NoDeviceError


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


class Device(object):
    def __init__(self, device_id):
        if type(device_id) == str:
            # convert into bytes()
            device_id = device_id.encode("utf-8")
        hd = HDHOMERUN_LIB.hdhomerun_device_create_from_str(device_id, None)

        if not hd:
            raise DeviceError("Invalid device id {}.".format(device_id))

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

    @staticmethod
    def from_discover_device(discover_device):
        return Device(utils.device_id_to_str(discover_device.device_id))

    def __repr__(self):
        return "<{} {} at {}>".format(self.__class__.__name__, self.id, self.ip)

    @property
    def id(self):
        return utils.device_id_to_str(self._id)

    @property
    def ip(self):
        return "{:d}.{:d}.{:d}.{:d}".format(
            self._ip >> 24 & 0x0FF,
            self._ip >> 16 & 0x0FF,
            self._ip >> 8 & 0x0FF,
            self._ip >> 4 & 0x0FF,
        )

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
    def version(self):
        return self.get(b"/sys/version")

    def get_tuner(self):
        return HDHOMERUN_LIB.hdhomerun_device_get_tuner(self._hd)

    def get(self, key):
        ret_value = pointer(c_char_p())
        ret_error = pointer(c_char_p())
        HDHOMERUN_LIB.hdhomerun_device_get_var(self._hd, key, ret_value, ret_error)

        if ret_error.contents:
            print(ret_error.contents.value.decode("utf-8"))

        print(ret_value.contents.value.decode("utf-8"))


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

    return [Device.from_discover_device(d) for i, d in enumerate(results) if i < devices_found]
