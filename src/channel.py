import os
from src.helpers import printj
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._youtube = build('youtube', 'v3', developerKey=Channel.api_key)
        self._channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = self._youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        printj(channel)
