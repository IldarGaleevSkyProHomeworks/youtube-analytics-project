import json

from googleapiclient.http import HttpMock
from src.channel import Channel
from pytest import fixture

import src.helpers

TEST_DATA_DIR = "tests/youtube_api_responses"

CHANNEL_LIST_RESPONSE_FILE = f'{TEST_DATA_DIR}/channels_list.json'


@fixture()
def google_api_mock_Channel():
    http = HttpMock(CHANNEL_LIST_RESPONSE_FILE, {'status': '200'})
    # Channel.api_key = "fake_api_key"
    Channel.http_lib = http
    yield Channel
    Channel.http_lib = None


@fixture()
def youtube_api_responses_channels_list():
    with open(CHANNEL_LIST_RESPONSE_FILE) as file:
        return json.load(file)


def test_print_info(google_api_mock_Channel, youtube_api_responses_channels_list, mocker):
    mocker.patch('src.helpers.printj')
    ch = google_api_mock_Channel("123")
    ch.print_info()
    src.helpers.printj.assert_called_once_with(youtube_api_responses_channels_list)
