import os.path
import shutil

from tests.helpers.http_mock_from_file import HttpMockFromFile
from src.youtube_api_object import YoutubeAPIObject
from pytest import fixture

FAKE_FS_PATH = "fakefs/"
TEST_DATA_DIR = "tests/youtube_api_responses"

YOUTUBE_API_RESPONSE_FILE = f'{TEST_DATA_DIR}/yt_api_mock.json'


@fixture()
def google_api_mock_http():
    http = HttpMockFromFile(YOUTUBE_API_RESPONSE_FILE)
    YoutubeAPIObject.http_lib = http
    YoutubeAPIObject.get_service(True)
    yield YoutubeAPIObject
    YoutubeAPIObject.http_lib = None
    YoutubeAPIObject._youtube = None


@fixture()
def fake_fs():
    if os.path.exists(FAKE_FS_PATH):
        shutil.rmtree(FAKE_FS_PATH)
    os.makedirs(FAKE_FS_PATH, exist_ok=True)
    yield FAKE_FS_PATH
