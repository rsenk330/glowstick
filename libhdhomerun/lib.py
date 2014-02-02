import ctypes
import sys

from .structs import hdhomerun_device_t, hdhomerun_debug_t, hdhomerun_discover_device_t
from .structs import hdhomerun_tuner_status_t, hdhomerun_tuner_vstatus_t, hdhomerun_plotsample_t
from .structs import hdhomerun_channelscan_result_t, hdhomerun_control_sock_t, hdhomerun_video_stats_t
from .structs import hdhomerun_video_sock_t

# Load library
libs = ('libhdhomerun.so', 'hdhomerun.so')
if sys.platform == "darwin":
    libs += ('libhdhomerun.dylib', 'hdhomerun.dylib')

HDHOMERUN_LIB = None
for lib in libs:
    try:
        HDHOMERUN_LIB = ctypes.cdll.LoadLibrary(lib)
        break
    except OSError:
        continue

if HDHOMERUN_LIB is None:
    raise OSError("Could not load libhdhomerun. Tried: {0}".format(", ".join(libs)))

hdhomerun_device_create = HDHOMERUN_LIB.hdhomerun_device_create
hdhomerun_device_create.argtypes = [ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint, ctypes.POINTER(hdhomerun_debug_t)]
hdhomerun_device_create.restype = ctypes.POINTER(hdhomerun_device_t)

hdhomerun_device_create_from_str = HDHOMERUN_LIB.hdhomerun_device_create_from_str
hdhomerun_device_create_from_str.argtypes = [ctypes.c_char_p, ctypes.POINTER(hdhomerun_debug_t)]
hdhomerun_device_create_from_str.restype = ctypes.POINTER(hdhomerun_device_t)

hdhomerun_device_destroy = HDHOMERUN_LIB.hdhomerun_device_destroy
hdhomerun_device_destroy.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_destroy.restype = None

hdhomerun_device_get_name = HDHOMERUN_LIB.hdhomerun_device_get_name
hdhomerun_device_get_name.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_get_name.restype = ctypes.c_char_p

hdhomerun_device_get_device_id = HDHOMERUN_LIB.hdhomerun_device_get_device_id
hdhomerun_device_get_device_id.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_get_device_id.restype = ctypes.c_uint32

hdhomerun_device_get_device_ip = HDHOMERUN_LIB.hdhomerun_device_get_device_ip
hdhomerun_device_get_device_ip.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_get_device_ip.restype = ctypes.c_uint32

hdhomerun_device_get_device_id_requested = HDHOMERUN_LIB.hdhomerun_device_get_device_id_requested
hdhomerun_device_get_device_id_requested.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_get_device_id_requested.restype = ctypes.c_uint32

hdhomerun_device_get_device_ip_requested = HDHOMERUN_LIB.hdhomerun_device_get_device_ip_requested
hdhomerun_device_get_device_ip_requested.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_get_device_ip_requested.restype = ctypes.c_uint32

hdhomerun_device_get_tuner = HDHOMERUN_LIB.hdhomerun_device_get_tuner
hdhomerun_device_get_tuner.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_get_tuner.restype = ctypes.c_uint

hdhomerun_device_set_device = HDHOMERUN_LIB.hdhomerun_device_set_device
hdhomerun_device_set_device.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_uint32, ctypes.c_uint32]
hdhomerun_device_set_device.restype = ctypes.c_int

hdhomerun_device_set_tuner = HDHOMERUN_LIB.hdhomerun_device_set_tuner
hdhomerun_device_set_tuner.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_uint]
hdhomerun_device_set_tuner.restype = ctypes.c_int

hdhomerun_device_set_tuner_from_str = HDHOMERUN_LIB.hdhomerun_device_set_tuner_from_str
hdhomerun_device_set_tuner_from_str.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_char_p]
hdhomerun_device_set_tuner_from_str.restype = ctypes.c_int

hdhomerun_device_get_local_machine_addr = HDHOMERUN_LIB.hdhomerun_device_get_local_machine_addr
hdhomerun_device_get_local_machine_addr.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_get_local_machine_addr.restype = ctypes.c_uint32

hdhomerun_device_get_tuner_status = HDHOMERUN_LIB.hdhomerun_device_get_tuner_status
hdhomerun_device_get_tuner_status.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(hdhomerun_tuner_status_t)]
hdhomerun_device_get_tuner_status.restype = ctypes.c_int

hdhomerun_device_get_tuner_vstatus = HDHOMERUN_LIB.hdhomerun_device_get_tuner_vstatus
hdhomerun_device_get_tuner_vstatus.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(hdhomerun_tuner_vstatus_t)]
hdhomerun_device_get_tuner_vstatus.restype = ctypes.c_int

hdhomerun_device_get_tuner_streaminfo = HDHOMERUN_LIB.hdhomerun_device_get_tuner_streaminfo
hdhomerun_device_get_tuner_streaminfo.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p)]
hdhomerun_device_get_tuner_streaminfo.restype = ctypes.c_int

hdhomerun_device_get_tuner_channel = HDHOMERUN_LIB.hdhomerun_device_get_tuner_channel
hdhomerun_device_get_tuner_channel.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p)]
hdhomerun_device_get_tuner_channel.restype = ctypes.c_int

hdhomerun_device_get_tuner_vchannel = HDHOMERUN_LIB.hdhomerun_device_get_tuner_vchannel
hdhomerun_device_get_tuner_vchannel.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p)]
hdhomerun_device_get_tuner_vchannel.restype = ctypes.c_int

hdhomerun_device_get_tuner_channelmap = HDHOMERUN_LIB.hdhomerun_device_get_tuner_channelmap
hdhomerun_device_get_tuner_channelmap.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p)]
hdhomerun_device_get_tuner_channelmap.restype = ctypes.c_int

hdhomerun_device_get_tuner_filter = HDHOMERUN_LIB.hdhomerun_device_get_tuner_filter
hdhomerun_device_get_tuner_filter.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p)]
hdhomerun_device_get_tuner_filter.restype = ctypes.c_int

hdhomerun_device_get_tuner_program = HDHOMERUN_LIB.hdhomerun_device_get_tuner_program
hdhomerun_device_get_tuner_program.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p)]
hdhomerun_device_get_tuner_program.restype = ctypes.c_int

hdhomerun_device_get_tuner_target = HDHOMERUN_LIB.hdhomerun_device_get_tuner_target
hdhomerun_device_get_tuner_target.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p)]
hdhomerun_device_get_tuner_target.restype = ctypes.c_int

hdhomerun_device_get_tuner_plotsample = HDHOMERUN_LIB.hdhomerun_device_get_tuner_plotsample
hdhomerun_device_get_tuner_plotsample.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.POINTER(hdhomerun_plotsample_t)), ctypes.POINTER(ctypes.c_size_t)]
hdhomerun_device_get_tuner_plotsample.restype = ctypes.c_int

hdhomerun_device_get_oob_status = HDHOMERUN_LIB.hdhomerun_device_get_oob_status
hdhomerun_device_get_oob_status.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(hdhomerun_tuner_status_t)]
hdhomerun_device_get_oob_status.restype = ctypes.c_int

hdhomerun_device_get_oob_plotsample = HDHOMERUN_LIB.hdhomerun_device_get_oob_plotsample
hdhomerun_device_get_oob_plotsample.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.POINTER(hdhomerun_plotsample_t)), ctypes.POINTER(ctypes.c_size_t)]
hdhomerun_device_get_oob_plotsample.restype = ctypes.c_int

hdhomerun_device_get_tuner_lockkey_owner = HDHOMERUN_LIB.hdhomerun_device_get_tuner_lockkey_owner
hdhomerun_device_get_tuner_lockkey_owner.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p)]
hdhomerun_device_get_tuner_lockkey_owner.restype = ctypes.c_int

hdhomerun_device_get_ir_target = HDHOMERUN_LIB.hdhomerun_device_get_ir_target
hdhomerun_device_get_ir_target.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p)]
hdhomerun_device_get_ir_target.restype = ctypes.c_int

hdhomerun_device_get_lineup_location = HDHOMERUN_LIB.hdhomerun_device_get_lineup_location
hdhomerun_device_get_lineup_location.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p)]
hdhomerun_device_get_lineup_location.restype = ctypes.c_int

hdhomerun_device_get_version = HDHOMERUN_LIB.hdhomerun_device_get_version
hdhomerun_device_get_version.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_int32)]
hdhomerun_device_get_version.restype = ctypes.c_int

hdhomerun_device_get_supported = HDHOMERUN_LIB.hdhomerun_device_get_supported
hdhomerun_device_get_supported.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char), ctypes.POINTER(ctypes.c_char_p)]
hdhomerun_device_get_supported.restype = ctypes.c_int

hdhomerun_device_get_tuner_status_ss_color = HDHOMERUN_LIB.hdhomerun_device_get_tuner_status_ss_color
hdhomerun_device_get_tuner_status_ss_color.argtypes = [ctypes.POINTER(hdhomerun_tuner_status_t)]
hdhomerun_device_get_tuner_status_ss_color.restype = ctypes.c_uint32

hdhomerun_device_get_tuner_status_snq_color = HDHOMERUN_LIB.hdhomerun_device_get_tuner_status_snq_color
hdhomerun_device_get_tuner_status_snq_color.argtypes = [ctypes.POINTER(hdhomerun_tuner_status_t)]
hdhomerun_device_get_tuner_status_snq_color.restype = ctypes.c_uint32

hdhomerun_device_get_tuner_status_seq_color = HDHOMERUN_LIB.hdhomerun_device_get_tuner_status_seq_color
hdhomerun_device_get_tuner_status_seq_color.argtypes = [ctypes.POINTER(hdhomerun_tuner_status_t)]
hdhomerun_device_get_tuner_status_seq_color.restype = ctypes.c_uint32

hdhomerun_device_get_model_str = HDHOMERUN_LIB.hdhomerun_device_get_model_str
hdhomerun_device_get_model_str.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_get_model_str.restype = ctypes.c_char_p

hdhomerun_device_set_tuner_channel = HDHOMERUN_LIB.hdhomerun_device_set_tuner_channel
hdhomerun_device_set_tuner_channel.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_char_p]
hdhomerun_device_set_tuner_channel.restype = ctypes.c_int

hdhomerun_device_set_tuner_vchannel = HDHOMERUN_LIB.hdhomerun_device_set_tuner_vchannel
hdhomerun_device_set_tuner_vchannel.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_char_p]
hdhomerun_device_set_tuner_vchannel.restype = ctypes.c_int

hdhomerun_device_set_tuner_filter = HDHOMERUN_LIB.hdhomerun_device_set_tuner_filter
hdhomerun_device_set_tuner_filter.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_char_p]
hdhomerun_device_set_tuner_filter.restype = ctypes.c_int

hdhomerun_device_set_tuner_program = HDHOMERUN_LIB.hdhomerun_device_set_tuner_program
hdhomerun_device_set_tuner_program.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_char_p]
hdhomerun_device_set_tuner_program.restype = ctypes.c_int

hdhomerun_device_set_tuner_target = HDHOMERUN_LIB.hdhomerun_device_set_tuner_target
hdhomerun_device_set_tuner_target.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_char_p]
hdhomerun_device_set_tuner_target.restype = ctypes.c_int

hdhomerun_device_set_lineup_location = HDHOMERUN_LIB.hdhomerun_device_set_lineup_location
hdhomerun_device_set_lineup_location.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_char_p]
hdhomerun_device_set_lineup_location.restype = ctypes.c_int

hdhomerun_device_set_sys_dvbc_modulation = HDHOMERUN_LIB.hdhomerun_device_set_sys_dvbc_modulation
hdhomerun_device_set_sys_dvbc_modulation.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_char_p]
hdhomerun_device_set_sys_dvbc_modulation.restype = ctypes.c_int

hdhomerun_device_set_ir_target = HDHOMERUN_LIB.hdhomerun_device_set_ir_target
hdhomerun_device_set_ir_target.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_char_p]
hdhomerun_device_set_ir_target.restype = ctypes.c_int

hdhomerun_device_get_var = HDHOMERUN_LIB.hdhomerun_device_get_var
hdhomerun_device_get_var.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_char_p)]
hdhomerun_device_get_var.restype = ctypes.c_int

hdhomerun_device_set_var = HDHOMERUN_LIB.hdhomerun_device_set_var
hdhomerun_device_set_var.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_char_p, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_char_p)]
hdhomerun_device_set_var.restype = ctypes.c_int

hdhomerun_device_tuner_lockkey_request = HDHOMERUN_LIB.hdhomerun_device_tuner_lockkey_request
hdhomerun_device_tuner_lockkey_request.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(ctypes.c_char_p)]
hdhomerun_device_tuner_lockkey_request.restype = ctypes.c_int

hdhomerun_device_tuner_lockkey_release = HDHOMERUN_LIB.hdhomerun_device_tuner_lockkey_release
hdhomerun_device_tuner_lockkey_release.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_tuner_lockkey_release.restype = ctypes.c_int

hdhomerun_device_tuner_lockkey_force = HDHOMERUN_LIB.hdhomerun_device_tuner_lockkey_force
hdhomerun_device_tuner_lockkey_force.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_tuner_lockkey_force.restype = ctypes.c_int

hdhomerun_device_tuner_lockkey_use_value = HDHOMERUN_LIB.hdhomerun_device_tuner_lockkey_use_value
hdhomerun_device_tuner_lockkey_use_value.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_uint32]
hdhomerun_device_tuner_lockkey_use_value.restype = None

hdhomerun_device_wait_for_lock = HDHOMERUN_LIB.hdhomerun_device_wait_for_lock
hdhomerun_device_wait_for_lock.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(hdhomerun_tuner_status_t)]
hdhomerun_device_wait_for_lock.restype = ctypes.c_int

hdhomerun_device_stream_start = HDHOMERUN_LIB.hdhomerun_device_stream_start
hdhomerun_device_stream_start.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_stream_start.restype = ctypes.c_int

hdhomerun_device_stream_recv = HDHOMERUN_LIB.hdhomerun_device_stream_recv
hdhomerun_device_stream_recv.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)]
hdhomerun_device_stream_recv.restype = ctypes.POINTER(ctypes.c_uint8)

hdhomerun_device_stream_flush = HDHOMERUN_LIB.hdhomerun_device_stream_flush
hdhomerun_device_stream_flush.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_stream_flush.restype = ctypes.c_int

hdhomerun_device_stream_stop = HDHOMERUN_LIB.hdhomerun_device_stream_stop
hdhomerun_device_stream_stop.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_stream_stop.restype = ctypes.c_int

hdhomerun_device_channelscan_init = HDHOMERUN_LIB.hdhomerun_device_channelscan_init
hdhomerun_device_channelscan_init.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.c_char_p]
hdhomerun_device_channelscan_init.restype = ctypes.c_int

hdhomerun_device_channelscan_advance = HDHOMERUN_LIB.hdhomerun_device_channelscan_advance
hdhomerun_device_channelscan_advance.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(hdhomerun_channelscan_result_t)]
hdhomerun_device_channelscan_advance.restype = ctypes.c_int

hdhomerun_device_channelscan_detect = HDHOMERUN_LIB.hdhomerun_device_channelscan_detect
hdhomerun_device_channelscan_detect.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(hdhomerun_channelscan_result_t)]
hdhomerun_device_channelscan_detect.restype = ctypes.c_int

hdhomerun_device_channelscan_get_progress = HDHOMERUN_LIB.hdhomerun_device_channelscan_get_progress
hdhomerun_device_channelscan_get_progress.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_channelscan_get_progress.restype = ctypes.c_uint8

hdhomerun_device_get_control_sock = HDHOMERUN_LIB.hdhomerun_device_get_control_sock
hdhomerun_device_get_control_sock.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_get_control_sock.restype = ctypes.POINTER(hdhomerun_control_sock_t)

hdhomerun_device_get_video_sock = HDHOMERUN_LIB.hdhomerun_device_get_video_sock
hdhomerun_device_get_video_sock.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_get_video_sock.restype = ctypes.POINTER(hdhomerun_video_sock_t)

hdhomerun_device_debug_print_video_stats = HDHOMERUN_LIB.hdhomerun_device_debug_print_video_stats
hdhomerun_device_debug_print_video_stats.argtypes = [ctypes.POINTER(hdhomerun_device_t)]
hdhomerun_device_debug_print_video_stats.restype = None

hdhomerun_device_get_video_stats = HDHOMERUN_LIB.hdhomerun_device_get_video_stats
hdhomerun_device_get_video_stats.argtypes = [ctypes.POINTER(hdhomerun_device_t), ctypes.POINTER(hdhomerun_video_stats_t)]
hdhomerun_device_get_video_stats.restype = None

hdhomerun_discover_find_devices_custom = HDHOMERUN_LIB.hdhomerun_discover_find_devices_custom
hdhomerun_discover_find_devices_custom.argtypes = [ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(hdhomerun_discover_device_t), ctypes.c_int]
hdhomerun_discover_find_devices_custom.restype = ctypes.c_int

hdhomerun_discover_create = HDHOMERUN_LIB.hdhomerun_discover_create
hdhomerun_discover_create.argtypes = [ctypes.POINTER(hdhomerun_debug_t)]
hdhomerun_discover_create.restype = hdhomerun_discover_device_t

hdhomerun_discover_destroy = HDHOMERUN_LIB.hdhomerun_discover_destroy
hdhomerun_discover_destroy.argtypes = [ctypes.POINTER(hdhomerun_discover_device_t)]
hdhomerun_discover_destroy.restype = None

hdhomerun_discover_find_devices = HDHOMERUN_LIB.hdhomerun_discover_find_devices
hdhomerun_discover_find_devices.argtypes = [ctypes.POINTER(hdhomerun_discover_device_t), ctypes.c_uint32, ctypes.c_uint32, ctypes.c_uint32, ctypes.POINTER(hdhomerun_discover_device_t), ctypes.c_int]
hdhomerun_discover_find_devices.restype = ctypes.c_int

hdhomerun_discover_validate_device_id = HDHOMERUN_LIB.hdhomerun_discover_validate_device_id
hdhomerun_discover_validate_device_id.argtypes = [ctypes.c_uint32]
hdhomerun_discover_validate_device_id.restype = ctypes.c_int32

hdhomerun_discover_is_ip_multicast = HDHOMERUN_LIB.hdhomerun_discover_is_ip_multicast
hdhomerun_discover_is_ip_multicast.argtypes = [ctypes.c_uint32]
hdhomerun_discover_is_ip_multicast.restype = ctypes.c_int32

hdhomerun_channelmap_get_channelmap_scan_group = HDHOMERUN_LIB.hdhomerun_channelmap_get_channelmap_scan_group
hdhomerun_channelmap_get_channelmap_scan_group.argtypes = [ctypes.c_char_p]
hdhomerun_channelmap_get_channelmap_scan_group.restype = ctypes.c_char_p
