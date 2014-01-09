import inspect

from ctypes import c_char_p, pointer

from . import utils
from . import wrapper


class HDHomeRunLibrary:
    """Calls any known functions.

        lib = HDHomeRunLibrary()
        lib.hdhomerun_device_get_device_ip(hd)

    """

    def __getattr__(self, name):
        attr = getattr(wrapper, name)
        if attr:
            if hasattr(attr, "__call__") and not inspect.isclass(attr):
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
            raise Exception("Invalid device id {}.".format(device_id))

        # Device ID check
        device_id_requested = HDHOMERUN_LIB.hdhomerun_device_get_device_id_requested(hd)
        if not HDHOMERUN_LIB.hdhomerun_discover_validate_device_id(device_id_requested):
            raise Exception("Invalid device id: {}".format(device_id_requested))

        # Connect to device and check model
        model = HDHOMERUN_LIB.hdhomerun_device_get_model_str(hd)
        if not model:
            HDHOMERUN_LIB.hdhomerun_device_destroy(hd)
            raise Exception("Unable to connect to device")

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

    def get(self, key):
        ret_value = pointer(c_char_p())
        ret_error = pointer(c_char_p())
        HDHOMERUN_LIB.hdhomerun_device_get_var(self._hd, key, ret_value, ret_error)

        if ret_error.contents:
            print(ret_error.contents.value.decode("utf-8"))

        print(ret_value.contents.value.decode("utf-8"))


def get_devices():
    results = (HDHOMERUN_LIB.hdhomerun_discover_device_t * 64)()
    devices_found = HDHOMERUN_LIB.hdhomerun_discover_find_devices_custom(
        0,
        HDHOMERUN_LIB.HDHOMERUN_DEVICE_TYPE_TUNER,
        HDHOMERUN_LIB.HDHOMERUN_DEVICE_ID_WILDCARD,
        results,
        64
    )

    if devices_found < 0:
        print("Error discovering devices")
        return []
    elif devices_found == 0:
        print("No devices found")
        return []

    return [Device.from_discover_device(d) for i, d in enumerate(results) if i < devices_found]
