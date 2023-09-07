import json
import src.helpers
from src.youtube_api_object import YoutubeAPIObject


class Channel(YoutubeAPIObject):
    """Youtube channel"""
    channel_url = f'{YoutubeAPIObject.base_url}/channel'

    _PART_CHANNEL_INFO = "Channel"

    def __init__(self, channel_id: str) -> None:
        """
        :param channel_id: channel id
        """

        super().__init__()
        self._channel_id = channel_id

        self._set_request_obj(
            Channel._PART_CHANNEL_INFO,
            YoutubeAPIObject.get_service().channels().list(
                id=self._channel_id,
                part='snippet,statistics'
            )
        )

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.subscriber_count + other.subscriber_count
        raise TypeError(f"Second operand must be a {self.__class__.__name__}")

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.subscriber_count - other.subscriber_count
        raise TypeError(f"Second operand must be a {self.__class__.__name__}")

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.subscriber_count == other.subscriber_count
        raise TypeError(f"Second operand must be a {self.__class__.__name__}")

    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.subscriber_count <= other.subscriber_count
        raise TypeError(f"Second operand must be a {self.__class__.__name__}")

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.subscriber_count < other.subscriber_count
        raise TypeError(f"Second operand must be a {self.__class__.__name__}")

    def print_info(self) -> None:
        """Printing channel info"""

        src.helpers.printj(self._api_object_info_raw(Channel._PART_CHANNEL_INFO))

    @property
    def channel_info(self):
        """ channel info """
        return self._api_object_info_raw(Channel._PART_CHANNEL_INFO)["items"][0]

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

    @property
    def subscriber_count(self):
        """ video count """
        return int(self.channel_info["statistics"]["subscriberCount"])

    def to_json(self, filename):
        """
        save channel info to json file
        :param filename: target file
        """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.channel_info, file)
