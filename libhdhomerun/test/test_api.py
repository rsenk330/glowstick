import pytest
from unittest import mock

from libhdhomerun import lib as HOMERUN_LIB


@pytest.fixture
def lib():
    from libhdhomerun import api
    return api.HDHomeRunLibrary()


@pytest.fixture
def device_mock():
    return mock.Mock()


@pytest.fixture
def discover_device_mock(request):
    patcher = mock.patch("libhdhomerun.api.hdhomerun_discover_device_t")
    hdhomerun_discover_device_t = patcher.start()

    request.addfinalizer(lambda: patcher.stop())

    discover_device_mock = mock.Mock()
    discover_device_mock.tuner_count = 2
    discover_device_mock.ip_addr = 2130706433
    discover_device_mock.device_id = 0x12345
    hdhomerun_discover_device_t.return_value = discover_device_mock

    return discover_device_mock


@pytest.fixture
def hdhomerun_lib(request, device_mock):
    patcher = mock.patch("libhdhomerun.api.HDHOMERUN_LIB")
    hdhomerun_lib = patcher.start()

    hdhomerun_lib.hdhomerun_discover_find_devices_custom.return_value = 1
    hdhomerun_lib.hdhomerun_device_get_device_id_requested.return_value = 0x12345
    hdhomerun_lib.hdhomerun_discover_validate_device_id.return_value = True
    hdhomerun_lib.hdhomerun_device_get_model_str.return_value = "TEST HD <Mock>"
    hdhomerun_lib.hdhomerun_device_create_from_str.return_value = device_mock
    hdhomerun_lib.hdhomerun_device_get_var.return_value = None
    hdhomerun_lib.hdhomerun_device_get_tuner.return_value = "Test get_tuner() return value"
    hdhomerun_lib.hdhomerun_device_get_lineup_location.return_value = "Test get_lineup_location() return value"


    request.addfinalizer(lambda: patcher.stop())

    return hdhomerun_lib


@pytest.fixture
def device(device_mock, discover_device_mock, hdhomerun_lib):
    from libhdhomerun.api import Device
    return Device(device_ip="127.0.0.1")


@pytest.fixture
def device_mocked_get(request, device, device_mock, discover_device_mock, hdhomerun_lib):
    patcher = mock.patch("libhdhomerun.api.Device.get")
    get = patcher.start()
    get.return_value = "Test get() return value"

    device.get = get

    request.addfinalizer(lambda: patcher.stop())

    return device


def test_hdhomerunlibrary_getattr_valid_method(lib):
    assert lib.hdhomerun_device_create == HOMERUN_LIB.hdhomerun_device_create


def test_hdhomerunlibrary_getattr_valid_variable(lib):
    assert lib.HDHOMERUN_LIB == HOMERUN_LIB.HDHOMERUN_LIB


def test_hdhomerunlibrary_getattr_invalid(lib):
    with pytest.raises(AttributeError):
        lib.invalid_method()


def test_hdhomerunlibrary_getattr_valid_instance_variable(lib):
    lib.test_variable = "TEST"
    assert lib.test_variable == "TEST"


def test_device_create_device_id_int(device_mock, discover_device_mock, hdhomerun_lib):
    from libhdhomerun import constants
    from libhdhomerun.api import Device

    Device(device_id=74565)

    hdhomerun_lib.hdhomerun_discover_find_devices_custom.assert_called_once_with(
        0, constants.HDHOMERUN_DEVICE_TYPE_WILDCARD, 74565, discover_device_mock, 1
    )
    hdhomerun_lib.hdhomerun_device_create_from_str.assert_called_once_with(b"   12345", None)
    hdhomerun_lib.hdhomerun_device_get_device_id_requested.assert_called_once_with(device_mock)
    hdhomerun_lib.hdhomerun_discover_validate_device_id.assert_called_once_with(0x12345)
    hdhomerun_lib.hdhomerun_device_get_model_str.assert_called_once_with(device_mock)
    assert not hdhomerun_lib.hdhomerun_device_destroy.called


def test_device_create_device_ip_int(device_mock, discover_device_mock, hdhomerun_lib):
    from libhdhomerun import constants
    from libhdhomerun.api import Device

    Device(device_ip=2130706433)

    hdhomerun_lib.hdhomerun_discover_find_devices_custom.assert_called_once_with(
        2130706433, constants.HDHOMERUN_DEVICE_TYPE_WILDCARD, 0, discover_device_mock, 1
    )
    hdhomerun_lib.hdhomerun_device_create_from_str.assert_called_once_with(b"       0", None)
    hdhomerun_lib.hdhomerun_device_get_device_id_requested.assert_called_once_with(device_mock)
    hdhomerun_lib.hdhomerun_discover_validate_device_id.assert_called_once_with(0x12345)
    hdhomerun_lib.hdhomerun_device_get_model_str.assert_called_once_with(device_mock)
    assert not hdhomerun_lib.hdhomerun_device_destroy.called


def test_device_create_device_ip_str(device_mock, discover_device_mock, hdhomerun_lib):
    from libhdhomerun import constants
    from libhdhomerun.api import Device

    Device(device_ip="127.0.0.1")

    hdhomerun_lib.hdhomerun_discover_find_devices_custom.assert_called_once_with(
        2130706433, constants.HDHOMERUN_DEVICE_TYPE_WILDCARD, 0, discover_device_mock, 1
    )
    hdhomerun_lib.hdhomerun_device_create_from_str.assert_called_once_with(b"       0", None)
    hdhomerun_lib.hdhomerun_device_get_device_id_requested.assert_called_once_with(device_mock)
    hdhomerun_lib.hdhomerun_discover_validate_device_id.assert_called_once_with(0x12345)
    hdhomerun_lib.hdhomerun_device_get_model_str.assert_called_once_with(device_mock)
    assert not hdhomerun_lib.hdhomerun_device_destroy.called


def test_device_create_device_ip_multicast(device_mock, discover_device_mock, hdhomerun_lib):
    from libhdhomerun.api import Device

    with pytest.raises(ValueError):
        Device(device_ip=3758096385)  # 224.0.0.1


def test_device_id(device):
    assert device.id == "   12345"


def test_device_ip(device):
    assert device.ip == "127.0.0.1"


def test_device_tuner_count(device):
    assert device.tuner_count == 2


def test_device_copyright(device_mocked_get):
    assert device_mocked_get.copyright == "Test get() return value"
    device_mocked_get.get.assert_called_once_with(b"/sys/copyright")


def test_device_features(device_mocked_get):
    assert device_mocked_get.features == "Test get() return value"
    device_mocked_get.get.assert_called_once_with(b"/sys/features")


def test_device_hwmodel(device_mocked_get):
    assert device_mocked_get.hwmodel == "Test get() return value"
    device_mocked_get.get.assert_called_once_with(b"/sys/hwmodel")


def test_device_model(device_mocked_get):
    assert device_mocked_get.model == "Test get() return value"
    device_mocked_get.get.assert_called_once_with(b"/sys/model")


def test_device_version(device_mocked_get):
    assert device_mocked_get.version == "Test get() return value"
    device_mocked_get.get.assert_called_once_with(b"/sys/version")


def test_device_get_tuner(device, hdhomerun_lib):
    resp = device.get_tuner()
    hdhomerun_lib.hdhomerun_device_get_tuner.assert_called_once_with(device._hd)
    assert resp == "Test get_tuner() return value"


@mock.patch("libhdhomerun.api.byref")
@mock.patch("libhdhomerun.api.c_char_p")
def test_device_get_linup(c_char_p, byref, device, hdhomerun_lib):
    ref = mock.MagicMock()
    byref.return_value = ref

    instance = c_char_p.return_value
    type(instance).value = b"Test"
    resp = device.get_lineup()

    byref.assert_called_once_with(instance)
    hdhomerun_lib.hdhomerun_device_get_lineup_location.assert_called_once_with(device._hd, ref)
    assert resp == "Test"


def test_device_get_valid(device, hdhomerun_lib):
    with mock.patch("libhdhomerun.api.c_char_p") as c_char_p:
        instance = c_char_p.return_value
        type(instance).value = mock.PropertyMock(side_effect=[None, b"Test"])
        resp = device.get(b"/sys/copyright")

        hdhomerun_lib.hdhomerun_device_get_var.assert_called_once_with(device._hd, b"/sys/copyright", instance, instance)
        assert resp == "Test"


def test_device_get_invalid(device, hdhomerun_lib):
    from libhdhomerun.exceptions import DeviceError
    with mock.patch("libhdhomerun.api.c_char_p") as c_char_p:
        instance = c_char_p.return_value
        type(instance).value = mock.PropertyMock(side_effect=[b"Test", b"Test", None])

        with pytest.raises(DeviceError):
            device.get(b"/sys/copyright")

        hdhomerun_lib.hdhomerun_device_get_var.assert_called_once_with(device._hd, b"/sys/copyright", instance, instance)


def test_get_devices(hdhomerun_lib, discover_device_mock):
    from libhdhomerun.api import get_devices
    hdhomerun_lib.hdhomerun_discover_find_devices_custom.return_value = 1
    hdhomerun_lib.hdhomerun_discover_device_t.__mul__.return_value = mock.Mock(return_value=[discover_device_mock])

    devices = get_devices()

    assert hdhomerun_lib.hdhomerun_discover_find_devices_custom.call_count == 2  # Device __init__ calls it once, too
    assert len(devices) == 1
    assert devices[0]._id == 0x12345
    assert devices[0]._ip == 2130706433


def test_get_devices_none_found(hdhomerun_lib):
    from libhdhomerun.api import get_devices
    from libhdhomerun.exceptions import NoDeviceError
    hdhomerun_lib.hdhomerun_discover_find_devices_custom.return_value = 0

    with pytest.raises(NoDeviceError):
        devices = get_devices()
        assert devices == 0


def test_get_devices_error(discover_device_mock, hdhomerun_lib):
    from libhdhomerun.api import get_devices
    from libhdhomerun.exceptions import HomeRunError
    hdhomerun_lib.hdhomerun_discover_find_devices_custom.return_value = -1

    with pytest.raises(HomeRunError):
        devices = get_devices()
        assert devices == -1
