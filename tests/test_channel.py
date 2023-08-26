import json
import os.path
import shutil

from googleapiclient.http import HttpMock
from src.channel import Channel
from pytest import fixture

import src.helpers

FAKE_FS_PATH = "fakefs/"
TEST_DATA_DIR = "tests/youtube_api_responses"

CHANNEL_LIST_RESPONSE_FILE = f'{TEST_DATA_DIR}/channels_list.json'


@fixture()
def google_api_mock_Channel():
    http = HttpMock(CHANNEL_LIST_RESPONSE_FILE, {'status': '200'})
    # Channel.api_key = "fake_api_key"
    Channel.http_lib = http
    Channel.get_service(True)
    yield Channel
    Channel.http_lib = None
    Channel._youtube = None


@fixture()
def fake_fs():
    if os.path.exists(FAKE_FS_PATH):
        shutil.rmtree(FAKE_FS_PATH)
    os.makedirs(FAKE_FS_PATH, exist_ok=True)
    yield FAKE_FS_PATH


@fixture()
def youtube_api_responses_channels_list():
    with open(CHANNEL_LIST_RESPONSE_FILE) as file:
        return json.load(file)


def test_print_info(google_api_mock_Channel, youtube_api_responses_channels_list, mocker):
    mocker.patch('src.helpers.printj')
    ch = google_api_mock_Channel("123")
    ch.print_info()
    src.helpers.printj.assert_called_once_with(youtube_api_responses_channels_list)


def test_title_prop(google_api_mock_Channel):
    channel1 = google_api_mock_Channel('')
    assert channel1.title == 'ChannelName'


def test_video_count_prop(google_api_mock_Channel):
    channel1 = google_api_mock_Channel('')
    assert channel1.video_count == 5


def test_video_url_prop(google_api_mock_Channel):
    channel1 = google_api_mock_Channel('FAKE_CHANNEL_ID')

    assert channel1.url == f'{channel1.channel_url}/FAKE_CHANNEL_ID'


def test_video_to_json(google_api_mock_Channel, fake_fs):

    file_path = os.path.join(fake_fs, 'channel.json')
    channel1 = google_api_mock_Channel('')
    channel1.to_json(file_path)

    assert os.path.exists(file_path)
