import os.path

from pytest import raises

import src.helpers
from src.channel import Channel


def test_print_info(google_api_mock_http, mocker):
    mocker.patch('src.helpers.printj')
    ch = Channel("FAKE_CHANNEL_ID_WITH_SHORT_DATA")
    ch.print_info()
    src.helpers.printj.assert_called_once_with({"data": "test_response"})


def test_title_prop(google_api_mock_http):
    channel1 = Channel('FAKE_CHANNEL_1_ID')
    assert channel1.title == 'ChannelName'


def test_video_count_prop(google_api_mock_http):
    channel1 = Channel('FAKE_CHANNEL_1_ID')
    assert channel1.video_count == 5


def test_subscriber_count_prop(google_api_mock_http):
    channel1 = Channel('FAKE_CHANNEL_1_ID')
    assert channel1.subscriber_count == 200


def test_video_url_prop(google_api_mock_http):
    channel1 = Channel('FAKE_CHANNEL_1_ID')

    assert channel1.url == f'{channel1.channel_url}/FAKE_CHANNEL_1_ID'


def test_video_to_json(google_api_mock_http, fake_fs):
    file_path = os.path.join(fake_fs, 'channel.json')
    channel1 = Channel('FAKE_CHANNEL_1_ID')
    channel1.to_json(file_path)

    assert os.path.exists(file_path)


def test_str(google_api_mock_http):
    channel1 = Channel('FAKE_CHANNEL_1_ID')
    assert str(channel1) == f"ChannelName ({channel1.channel_url}/FAKE_CHANNEL_1_ID)"


def test_add(google_api_mock_http):
    channel1 = Channel('FAKE_CHANNEL_1_ID')
    channel2 = Channel('FAKE_CHANNEL_2_ID')

    assert channel1 + channel2 == 700

    with raises(TypeError):
        _ = channel1 + 3


def test_sub(google_api_mock_http):
    channel1 = Channel('FAKE_CHANNEL_1_ID')
    channel2 = Channel('FAKE_CHANNEL_2_ID')

    assert channel1 - channel2 == -300
    assert channel2 - channel1 == 300

    with raises(TypeError):
        _ = channel1 - 3


def test_equal(google_api_mock_http):
    channel1 = Channel('FAKE_CHANNEL_1_ID')
    channel2 = Channel('FAKE_CHANNEL_2_ID')
    channel3 = Channel('FAKE_CHANNEL_3_ID')

    assert channel1 != channel2
    assert channel2 == channel3

    with raises(TypeError):
        assert channel2 == 3


def test_lt(google_api_mock_http):
    channel1 = Channel('FAKE_CHANNEL_1_ID')
    channel2 = Channel('FAKE_CHANNEL_2_ID')
    channel3 = Channel('FAKE_CHANNEL_3_ID')

    assert channel1 < channel2
    assert not channel2 < channel3

    assert channel2 > channel1
    assert not channel2 > channel3

    with raises(TypeError):
        assert channel2 < 3


def test_le(google_api_mock_http):
    channel1 = Channel('FAKE_CHANNEL_1_ID')
    channel2 = Channel('FAKE_CHANNEL_2_ID')
    channel3 = Channel('FAKE_CHANNEL_3_ID')

    assert not channel1 >= channel2
    assert channel2 >= channel3

    assert channel1 <= channel2
    assert channel2 <= channel3

    with raises(TypeError):
        assert channel2 <= 3
