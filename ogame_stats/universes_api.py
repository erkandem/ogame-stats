import json
from .utils import ApiBaseClass


class UniversesDataUrls(ApiBaseClass):
    def _get_universes_url(self) -> str:
        return 'https://lobby.ogame.gameforge.com/api/servers'

    def _load_data(self, url):
        """overwrites parents because we receive json instead of xml"""
        url = self._get_universes_url()
        response = self._do_get(url)
        json_str = response.content.decode('utf-8')
        return json.loads(json_str)

    def load_universes_data(self):
        url = self._get_universes_url()
        return self._load_data_as_df(url)


class UniversesData:
    def __init__(self):
        self.urls = UniversesDataUrls()
        self.data = self.urls.load_universes_data()


class UniversesQuestions(UniversesData):
    pass
