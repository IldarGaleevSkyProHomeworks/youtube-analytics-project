import os
import src.helpers
from googleapiclient.discovery import build


class Channel:
    """Youtube channel"""
    http_lib = None
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """

        """

        self._youtube = build(
            serviceName='youtube',
            version='v3',
            developerKey=Channel.api_key,
            http=Channel.http_lib
        )

        self._channel_id = channel_id

    def print_info(self) -> None:
        """Printing channel info"""

        channel = self._youtube.channels().list(
            id=self._channel_id,
            part='snippet,statistics'
        ).execute()

        src.helpers.printj(channel)
