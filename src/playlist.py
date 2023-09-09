from datetime import timedelta

from src.video import PLVideo
from src.youtube_api_object import YoutubeAPIObject
from operator import attrgetter


class PlayList(YoutubeAPIObject):
    playlist_url = f'{YoutubeAPIObject.base_url}/playlist'

    _PART_PLAYLIST_INFO = "Playlist"
    _PART_PLAYLIST_ITEM_LIST_INFO = "PlaylistItemList"

    def __init__(self, playlist_id):
        super().__init__()

        self._playlist_id = playlist_id
        self._playlist_videos = None

        self._set_request_obj(
            PlayList._PART_PLAYLIST_INFO,
            YoutubeAPIObject.get_service().playlists().list(
                id=self._playlist_id,
                part='snippet'
            )
        )

        self._set_request_obj(
            PlayList._PART_PLAYLIST_ITEM_LIST_INFO,
            YoutubeAPIObject.get_service().playlistItems().list(
                playlistId=self._playlist_id,
                part='snippet'
            )
        )

    def __str__(self):
        return self.title

    @property
    def playlist_id(self):
        return self._playlist_id

    @property
    def playlist_info(self):
        """ video info """
        return self._api_object_info_raw(PlayList._PART_PLAYLIST_INFO)["items"][0]

    @property
    def playlist_video_list_info(self):
        """ video items info """
        return self._api_object_info_raw(PlayList._PART_PLAYLIST_ITEM_LIST_INFO)["items"]

    @property
    def title(self):
        """ video title """
        return self.playlist_info["snippet"]["title"]

    @property
    def url(self):
        """ video url """
        return f'{PlayList.playlist_url}?list={self._playlist_id}'

    @property
    def playlist_videos(self) -> list[PLVideo]:
        """ list of playlist videos """
        if self._playlist_videos is None:
            playlist_items = self.playlist_video_list_info
            self._playlist_videos = []
            for pl_item in playlist_items:
                new_plvideo = PLVideo(pl_item["snippet"]["resourceId"]["videoId"], self._playlist_id, False)
                self._playlist_videos.append(new_plvideo)

        return self._playlist_videos

    @property
    def total_duration(self) -> timedelta:
        """ playlist duration """
        durations = [video.video_duration for video in self.playlist_videos]
        return sum(durations, start=timedelta(0))

    def show_best_video(self) -> str | None:
        """ returns url for best video """
        sorted_video = sorted(self.playlist_videos, key=attrgetter('like_count'))
        if sorted_video:
            return sorted_video[-1].url
        return None
