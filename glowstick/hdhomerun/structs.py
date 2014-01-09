from ctypes import c_uint8, c_uint32
from ctypes import Structure


class hdhomerun_device_t(Structure):
    pass


class hdhomerun_debug_t(Structure):
    pass


class hdhomerun_discover_device_t(Structure):
    _fields_ = [
        ("ip_addr", c_uint32),
        ("device_type", c_uint32),
        ("device_id", c_uint32),
        ("tuner_count", c_uint8)
    ]
