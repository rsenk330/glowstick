HDHOMERUN_CHANNELSCAN_MAX_PROGRAM_COUNT = 64
HDHOMERUN_CHANNELSCAN_PROGRAM_CONTROL = 2
HDHOMERUN_CHANNELSCAN_PROGRAM_ENCRYPTED = 3
HDHOMERUN_CHANNELSCAN_PROGRAM_NODATA = 1
HDHOMERUN_CHANNELSCAN_PROGRAM_NORMAL = 0
HDHOMERUN_CONTROL_TCP_PORT = 65001
HDHOMERUN_DEVICE_ID_WILDCARD = 0xFFFFFFFF
HDHOMERUN_DEVICE_MAX_LOCK_TO_DATA_TIME = 2000
HDHOMERUN_DEVICE_MAX_TUNE_TO_LOCK_TIME = 1500
HDHOMERUN_DEVICE_MAX_TUNE_TO_DATA_TIME = HDHOMERUN_DEVICE_MAX_TUNE_TO_LOCK_TIME + HDHOMERUN_DEVICE_MAX_LOCK_TO_DATA_TIME
HDHOMERUN_DEVICE_TYPE_WILDCARD = 0xFFFFFFFF
HDHOMERUN_DEVICE_TYPE_TUNER = 0x00000001
HDHOMERUN_DISCOVER_UDP_PORT = 65001
HDHOMERUN_MAX_PACKET_SIZE = 1460
HDHOMERUN_MAX_PAYLOAD_SIZE = 1452
HDHOMERUN_MIN_PEEK_LENGTH = 4
HDHOMERUN_STATUS_COLOR_GREEN = 0xFF00C000
HDHOMERUN_STATUS_COLOR_NEUTRAL = 0xFFFFFFFF
HDHOMERUN_STATUS_COLOR_RED = 0xFFFF0000
HDHOMERUN_STATUS_COLOR_YELLOW = 0xFFFFFF00
HDHOMERUN_TAG_DEVICE_ID = 0x02
HDHOMERUN_TAG_DEVICE_TYPE = 0x01
HDHOMERUN_TAG_ERROR_MESSAGE = 0x05
HDHOMERUN_TAG_GETSET_LOCKKEY = 0x15
HDHOMERUN_TAG_GETSET_NAME = 0x03
HDHOMERUN_TAG_GETSET_VALUE = 0x04
HDHOMERUN_TAG_TUNER_COUNT = 0x10
HDHOMERUN_TARGET_PROTOCOL_UDP = "udp"
HDHOMERUN_TARGET_PROTOCOL_RTP = "rtp"
HDHOMERUN_TYPE_DISCOVER_REQ = 0x0002
HDHOMERUN_TYPE_DISCOVER_RPY = 0x0003
HDHOMERUN_TYPE_GETSET_REQ = 0x0004
HDHOMERUN_TYPE_GETSET_RPY = 0x0005
HDHOMERUN_TYPE_UPGRADE_REQ = 0x0006
HDHOMERUN_TYPE_UPGRADE_RPY = 0x0007
TS_PACKET_SIZE = 188
VIDEO_DATA_BUFFER_SIZE_1S = 20000000 / 8
VIDEO_DATA_PACKET_SIZE = 188 * 7
VIDEO_RTP_DATA_PACKET_SIZE = (188 * 7) + 12