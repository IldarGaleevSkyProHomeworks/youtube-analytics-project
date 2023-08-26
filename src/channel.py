import json
import os
import src.helpers
from googleapiclient.discovery import build


class Channel:
    """Youtube channel"""
    http_lib = None
    api_key: str = os.getenv('YT_API_KEY')
    base_url = r'https://www.youtube.com'
    channel_url = f'{base_url}/channel'
    _youtube = None

    @classmethod
    def get_service(cls, reload=False):
        """
        returns API service object
        :param reload: if True - rebuild API service object
        """
        if cls._youtube is None or reload:
            cls._youtube = build(
                serviceName='youtube',
                version='v3',
                developerKey=cls.api_key,
                http=cls.http_lib
            )
        return cls._youtube

    def __init__(self, channel_id: str) -> None:
        """
        :param channel_id: channel id
        """

        self._channel_info_raw = None
        self._channel_id = channel_id

    def print_info(self) -> None:
        """Printing channel info"""

        src.helpers.printj(self.channel_info_raw)

    def update_channel_info(self):
        """ force update channel info """
        self._channel_info_raw = Channel.get_service().channels().list(
            id=self._channel_id,
            part='snippet,statistics'
        ).execute()

    @property
    def channel_info_raw(self):
        """ full response json """
        if self._channel_info_raw is None:
            self.update_channel_info()
        return self._channel_info_raw

    @property
    def channel_info(self):
        """ channel info """
        return self.channel_info_raw["items"][0]

    @property
    def title(self):
        """ channel title """
        return self.channel_info["snippet"]["title"]

    @property
    def url(self):
        """ channel url """
        return f'{Channel.channel_url}/{self._channel_id}'

    @property
    def video_count(self):
        """ video count """
        return int(self.channel_info["statistics"]["videoCount"])

    def to_json(self, filename):
        """
        save channel info to json file
        :param filename: target file
        """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.channel_info, file)
