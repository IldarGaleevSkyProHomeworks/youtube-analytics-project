import os
from googleapiclient.discovery import build


class YoutubeAPIObject:
    http_lib = None
    api_key: str = os.getenv('YT_API_KEY')
    base_url = r'https://www.youtube.com'
    base_url_h1 = r'https://youtu.be'
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

    def __init__(self):
        self.__api_object_raw_info = {}
        self.__api_request = {}
        self._api_request_exception = None

    @property
    def api_request_exception(self):
        return self._api_request_exception

    def _set_request_obj(self, part, request_obj):
        self.__api_request[part] = request_obj

    def _update_api_object_info(self, part):
        """ force update api object info """
        api_request = self.__api_request.get(part, None)
        if api_request is None:
            raise NotImplementedError("Wrong API object implementation: request object is not changed")

        try:
            data = api_request.execute()
            if data["items"]:
                self.__api_object_raw_info[part] = data
            else:
                raise IndexError("API response: Items list is empty")
        except Exception as ex:
            self.__api_object_raw_info[part] = YoutubeDummyObject()
            self._api_request_exception = ex
        return self.__api_object_raw_info[part]

    def _api_object_info_raw(self, part):
        """ full response json """
        raw_info = self.__api_object_raw_info.get(part, None)
        if raw_info is None:
            raw_info = self._update_api_object_info(part)
        return raw_info


class YoutubeDummyObject:
    def __getitem__(self, item):
        return self
