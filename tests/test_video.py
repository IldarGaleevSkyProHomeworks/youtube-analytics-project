from datetime import timedelta

import pytest

from src.video import Video


@pytest.fixture
def video_fixture():
    return Video('FAKE_VIDEO_1_ID')


def test_video_title_prop(google_api_mock_http, video_fixture):
    assert video_fixture.title == 'Video1 title'


def test_video_video_id_prop(google_api_mock_http, video_fixture):
    assert video_fixture.video_id == 'FAKE_VIDEO_1_ID'


def test_video_str(google_api_mock_http, video_fixture):
    assert str(video_fixture) == 'Video1 title'


def test_video_video_url_prop(google_api_mock_http, video_fixture):
    assert video_fixture.url == f'{Video.video_url}/FAKE_VIDEO_1_ID'


def test_video_video_view_count_prop(google_api_mock_http, video_fixture):
    assert video_fixture.view_count == 100


def test_video_like_count_prop(google_api_mock_http, video_fixture):
    assert video_fixture.like_count == 10


def test_video_duration_prop(google_api_mock_http, video_fixture):
    assert video_fixture.video_duration == timedelta(minutes=56, seconds=24)


def test_video_unknown_video_id(google_api_mock_http):
    unknown_video = Video('FAKE_VIDEO_UNKNOWN_ID')

    assert unknown_video.video_id == 'FAKE_VIDEO_UNKNOWN_ID'
    assert unknown_video.title is None
    assert unknown_video.like_count is None
    assert unknown_video.video_duration is None
    assert unknown_video.view_count is None

    assert unknown_video.api_request_exception is not None
