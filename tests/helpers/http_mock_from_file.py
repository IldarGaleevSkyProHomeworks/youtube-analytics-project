import httplib2
import json
from urllib import parse


class HttpMockFromFile:
    """Create Mock HTTP from file"""
    def __init__(self, filename=None):
        if filename:
            with open(filename, "r") as f:
                self.data = json.load(f)
        else:
            self.data = None

        self.headers = None
        self.uri = None
        self.method = None
        self.body = None
        self.headers = None

    def get_response(self, path, query, method):
        method = method.upper()
        path_results = [dt[method] for dt in self.data if dt["endpoint"] == path and dt[method]][0]
        if path_results:
            for response in path_results:
                if response["query"] == query:
                    return response["response"]["headers"], response["response"]["body"]
        return None

    def request(
            self,
            uri,
            method="GET",
            body=None,
            headers=None,
            redirections=1,
            connection_type=None,
    ):

        url_info = parse.urlparse(uri)

        rsp = self.get_response(url_info.path, url_info.query, method)
        if rsp:
            a = rsp
            return httplib2.Response(rsp[0]), json.dumps(rsp[1])

        return httplib2.Response({'status': '400'}), None

    def close(self):
        return None
