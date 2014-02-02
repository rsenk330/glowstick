from ctypes import c_char, c_int16, c_int32, c_uint8, c_uint16, c_uint32
from ctypes import Structure

from .constants import HDHOMERUN_CHANNELSCAN_MAX_PROGRAM_COUNT


class hdhomerun_device_t(Structure):
    pass


class hdhomerun_debug_t(Structure):
    pass


class hdhomerun_control_sock_t(Structure):
    pass


class hdhomerun_video_sock_t(Structure):
    pass


class hdhomerun_video_stats_t(Structure):
    _fields_ = [
        ("packet_count", c_uint32),
        ("network_error_count", c_uint32),
        ("transport_error_count", c_uint32),
        ("sequence_error_count", c_uint32),
        ("overflow_error_count", c_uint32)
    ]


class hdhomerun_tuner_status_t(Structure):
    _fields_ = [
        ("channel", c_char * 32),
        ("lock_str", c_char * 32),
        ("signal_present", c_int32),
        ("lock_supported", c_int32),
        ("lock_unsupported", c_int32),
        ("signal_strength", c_uint32),
        ("signal_to_noise_quality", c_uint32),
        ("symbol_error_quality", c_uint32),
        ("raw_bits_per_second", c_uint32),
        ("packets_per_second", c_uint32)
    ]


class hdhomerun_tuner_vstatus_t(Structure):
    _fields_ = [
        ("vchannel", c_char * 32),
        ("name", c_char * 32),
        ("auth", c_char * 32),
        ("cci", c_char * 32),
        ("cgms", c_char * 32),
        ("not_subscribed", c_int32),
        ("not_available", c_int32),
        ("copy_protected", c_int32)
    ]


class hdhomerun_channelscan_program_t(Structure):
    _fields_ = [
        ("program", c_char * 64),
        ("program_number", c_uint16),
        ("virtual_major", c_uint16),
        ("virtual_minor", c_uint16),
        ("type", c_uint16),
        ("name", c_char * 32)
    ]


class hdhomerun_channelscan_result_t(Structure):
    _fields_ = [
        ("channel_str", c_char * 64),
        ("channelmap", c_uint32),
        ("frequency", c_uint32),
        ("status", hdhomerun_tuner_status_t),
        ("program_count", c_int32),
        ("programs", hdhomerun_channelscan_program_t * HDHOMERUN_CHANNELSCAN_MAX_PROGRAM_COUNT),
        ("transport_stream_id_detected", c_int32),
        ("transport_stream_id", c_uint16)
    ]


class hdhomerun_plotsample_t(Structure):
    _fields_ = [
        ("real", c_int16),
        ("imag", c_int16)
    ]


class hdhomerun_discover_device_t(Structure):
    _fields_ = [
        ("ip_addr", c_uint32),
        ("device_type", c_uint32),
        ("device_id", c_uint32),
        ("tuner_count", c_uint8)
    ]
