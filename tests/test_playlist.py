from datetime import timedelta

import pytest

from src.playlist import PlayList
from src.video import PLVideo, Video


@pytest.fixture
def playlist_fixture():
    return PlayList("FAKE_PLAYLIST_1_ID")


def test_playlist_title_prop_n_str(google_api_mock_http, playlist_fixture):
    assert playlist_fixture.title == str(playlist_fixture) == "Playlist1 title"


def test_playlist_id(google_api_mock_http, playlist_fixture):
    assert playlist_fixture.playlist_id == "FAKE_PLAYLIST_1_ID"


def test_playlist_videos_list(google_api_mock_http, playlist_fixture):
    _ = playlist_fixture.playlist_videos  # call http request
    videos = playlist_fixture.playlist_videos  # take from cache

    requests = google_api_mock_http.http_lib.request_list

    assert len(videos) == 3
    assert isinstance(videos[0], PLVideo)
    # !!! 4 if debug traced - repr call additional requests
    assert len(requests) == 1


def test_playlist_total_duration_prop(google_api_mock_http, playlist_fixture):
    assert playlist_fixture.total_duration == timedelta(minutes=86, seconds=24)


def test_playlist_show_best_video(google_api_mock_http, playlist_fixture):
    assert playlist_fixture.show_best_video() == f'{Video.video_url}/FAKE_VIDEO_1_ID'


def test_playlist_url_prop(google_api_mock_http, playlist_fixture):
    assert playlist_fixture.url == f"{PlayList.playlist_url}?list=FAKE_PLAYLIST_1_ID"
