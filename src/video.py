from src.youtube_api_object import YoutubeAPIObject


class Video(YoutubeAPIObject):
    video_url = f'{YoutubeAPIObject.base_url}/watch'

    _PART_VIDEO_INFO = "Video"

    def __init__(self, video_id):
        super().__init__()

        self._video_id = video_id

        self._set_request_obj(
            Video._PART_VIDEO_INFO,
            YoutubeAPIObject.get_service().videos().list(
                id=self._video_id,
                part='snippet,statistics'
            )
        )

    def __str__(self):
        return self.video_title

    @property
    def video_id(self):
        return self._video_id

    @property
    def video_info(self):
        """ video info """
        return self._api_object_info_raw(Video._PART_VIDEO_INFO)["items"][0]

    @property
    def video_title(self):
        """ video title """
        return self.video_info["snippet"]["title"]

    @property
    def view_count(self):
        """ view count """
        return int(self.video_info["statistics"]["viewCount"])

    @property
    def like_count(self):
        """ likes count """
        return int(self.video_info["statistics"]["likeCount"])

    @property
    def url(self):
        """ video url """
        return f'{Video.video_url}?v={self._video_id}'


class PLVideo(Video):
    _PART_PLVIDEO_INFO = "PlaylistItem"

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id=video_id)

        self._playlist_id = playlist_id

        self._set_request_obj(
            PLVideo._PART_PLVIDEO_INFO,
            YoutubeAPIObject.get_service().playlistItems().list(
                playlistId=playlist_id,
                videoId=video_id,
                part='contentDetails',
                maxResults=1,
            )
        )

        playlist_info = self.playlist_item_info
        if not playlist_info:
            raise Exception("The playlist does not contain this video")

    @property
    def playlist_id(self):
        return self._playlist_id

    @property
    def playlist_item_info(self):
        """ playlist item info """

        items = self._api_object_info_raw(PLVideo._PART_PLVIDEO_INFO)["items"]
        if len(items) == 0:
            return None
        return items[0]

