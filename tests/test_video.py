from src.video import Video


def test_video_title_prop(google_api_mock_http):
    video1 = Video('FAKE_VIDEO_1_ID')
    assert video1.video_title == 'Video title'


def test_video_video_id_prop(google_api_mock_http):
    video1 = Video('FAKE_VIDEO_1_ID')
    assert video1.video_id == 'FAKE_VIDEO_1_ID'


def test_video_str(google_api_mock_http):
    video1 = Video('FAKE_VIDEO_1_ID')
    assert str(video1) == 'Video title'


def test_video_video_url_prop(google_api_mock_http):
    video1 = Video('FAKE_VIDEO_1_ID')

    assert video1.url == f'{video1.video_url}?v=FAKE_VIDEO_1_ID'


def test_video_video_view_count_prop(google_api_mock_http):
    video1 = Video('FAKE_VIDEO_1_ID')
    assert video1.view_count == 100


def test_video_like_count_prop(google_api_mock_http):
    video1 = Video('FAKE_VIDEO_1_ID')
    assert video1.like_count == 10
