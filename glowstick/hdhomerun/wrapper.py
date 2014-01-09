import sys

from ctypes import c_char_p, c_int, c_uint32
from ctypes import cdll, POINTER

from .structs import hdhomerun_device_t, hdhomerun_debug_t, hdhomerun_discover_device_t

MOD = sys.modules[__name__]

# Load library
HDHOMERUN_LIB = cdll.LoadLibrary("libhdhomerun.dylib")

# Constants
HDHOMERUN_DEVICE_TYPE_TUNER = 0x00000001
HDHOMERUN_DEVICE_ID_WILDCARD = 0xFFFFFFFF

# Function definitions
hdhomerun_device_create_from_str = HDHOMERUN_LIB.hdhomerun_device_create_from_str
hdhomerun_device_create_from_str.argtypes = [c_char_p, POINTER(hdhomerun_debug_t)]
hdhomerun_device_create_from_str.restype = POINTER(hdhomerun_device_t)

hdhomerun_device_get_device_id_requested = HDHOMERUN_LIB.hdhomerun_device_get_device_id_requested
hdhomerun_device_get_device_id_requested.argtypes = [POINTER(hdhomerun_device_t)]
hdhomerun_device_get_device_id_requested.restype = c_uint32

hdhomerun_discover_validate_device_id = HDHOMERUN_LIB.hdhomerun_discover_validate_device_id
hdhomerun_discover_validate_device_id.argtypes = [c_uint32]
hdhomerun_discover_validate_device_id.restype = c_uint32

hdhomerun_device_get_model_str = HDHOMERUN_LIB.hdhomerun_device_get_model_str
hdhomerun_device_get_model_str.argtypes = [POINTER(hdhomerun_device_t)]
hdhomerun_device_get_model_str.restype = c_char_p

hdhomerun_device_destroy = HDHOMERUN_LIB.hdhomerun_device_destroy
hdhomerun_device_destroy.argtypes = [POINTER(hdhomerun_device_t)]
hdhomerun_device_destroy.restype = None

hdhomerun_device_get_var = HDHOMERUN_LIB.hdhomerun_device_get_var
hdhomerun_device_get_var.argtypes = [POINTER(hdhomerun_device_t), c_char_p, POINTER(c_char_p), POINTER(c_char_p)]
hdhomerun_device_get_var.restype = c_int

hdhomerun_device_get_device_ip = HDHOMERUN_LIB.hdhomerun_device_get_device_ip
hdhomerun_device_get_device_ip.argtypes = [POINTER(hdhomerun_device_t)]
hdhomerun_device_get_device_ip.restype = c_uint32

hdhomerun_discover_find_devices_custom = HDHOMERUN_LIB.hdhomerun_discover_find_devices_custom
hdhomerun_discover_find_devices_custom.argtypes = [c_uint32, c_uint32, c_uint32, POINTER(hdhomerun_discover_device_t), c_int]
hdhomerun_discover_find_devices_custom.restype = c_int
