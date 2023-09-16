import pytest

from src.video import PLVideo


def test_pl_video_title_prop(google_api_mock_http):
    pl_video1 = PLVideo('FAKE_VIDEO_1_ID', 'FAKE_PLAYLIST_1_ID')
    assert pl_video1.title == 'Video1 title'


def test_pl_video_raise_Exception(google_api_mock_http):
    with pytest.raises(Exception):
        _ = PLVideo('FAKE_VIDEO_2_ID', 'FAKE_PLAYLIST_1_ID')


def test_pl_video_playlist_id_prop(google_api_mock_http):
    pl_video1 = PLVideo('FAKE_VIDEO_1_ID', 'FAKE_PLAYLIST_1_ID')

    assert pl_video1.playlist_id == 'FAKE_PLAYLIST_1_ID'
