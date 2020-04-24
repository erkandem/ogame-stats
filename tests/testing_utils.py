from pathlib import Path
import zipfile
import pytest
import requests
from ogame_stats import utils


class Constants:
    universe_id = 162
    community = 'en'


class TestingFiles:
    """
    Subclass with this to overwrite actual HTTP request with
    the "cached" files for testing purposes
    """
    ARCHIVE_FILEPATH = Path('tests/testing_data/testing_data.zip')
    URL_TO_FILE_MAPPING = {
        'https://s162-en.ogame.gameforge.com/api/highscore.xml?category=1&type=0': 'highscore_162_en_1_0_20200422_170240_197857.xml',
        'https://s162-en.ogame.gameforge.com/api/highscore.xml?category=1&type=1': 'highscore_162_en_1_1_20200422_170240_348153.xml',
        'https://s162-en.ogame.gameforge.com/api/highscore.xml?category=1&type=2': 'highscore_162_en_1_2_20200422_170240_500826.xml',
        'https://s162-en.ogame.gameforge.com/api/highscore.xml?category=1&type=3': 'highscore_162_en_1_3_20200422_170240_665208.xml',
        'https://s162-en.ogame.gameforge.com/api/highscore.xml?category=1&type=4': 'highscore_162_en_1_4_20200422_170240_816050.xml',
        'https://s162-en.ogame.gameforge.com/api/highscore.xml?category=1&type=5': 'highscore_162_en_1_5_20200422_170240_975528.xml',
        'https://s162-en.ogame.gameforge.com/api/highscore.xml?category=1&type=6': 'highscore_162_en_1_6_20200422_170241_126518.xml',
        'https://s162-en.ogame.gameforge.com/api/highscore.xml?category=1&type=7': 'highscore_162_en_1_7_20200422_170241_295144.xml',
        'https://lobby.ogame.gameforge.com/api/servers': 'universes_20200422_171937_861597.json',
        'https://s162-en.ogame.gameforge.com/api/players.xml': 'players_162_en_20200422_165756_623433.xml',
        'https://s162-en.ogame.gameforge.com/api/alliances.xml': 'alliances_162_en_20200422_165757_062851.xml',
        'https://s162-en.ogame.gameforge.com/api/universe.xml': 'universe_162_en_20200422_165756_915643.xml',
        'https://s162-en.ogame.gameforge.com/api/localization.xml': 'localisatzion_162_en_20200424_122401_354285.xml',
        'https://s162-en.ogame.gameforge.com/api/playerData.xml?id=110008': 'playerdata_162_en_110008_20200424_123313_597067.xml',
        'https://s162-en.ogame.gameforge.com/api/serverData.xml': 'server_data_162_en_20200424_224101_525526.xml',
    }

    def get_file_path(self, url: str):
        if url not in self.URL_TO_FILE_MAPPING.keys():
            raise KeyError(
                f'got url `{url}`. Currently defined ones are {list(self.URL_TO_FILE_MAPPING)}.'
            )
        return self.URL_TO_FILE_MAPPING[url]

    def load_file(self, url: str) -> bytes:
        with zipfile.ZipFile(self.ARCHIVE_FILEPATH, 'r') as zf:
            file_name = self.get_file_path(url)
            data = zf.read(file_name)
        return data

    def load_file_as_str(self, url: str) -> str:
        return self.load_file(url).decode()

    def _do_get(self, url: str) -> requests.Response:
        """
        Compatibility wrapper for ApiBaseClass.
        Spit out a fake response object with real but old data.
        """
        data = self.load_file(url)
        response = requests.Response()
        response._content = data
        return response

    def get(self, url: str) -> requests.Response:
        return self._do_get(url)


@pytest.fixture
def mock_requests(monkeypatch):
    monkeypatch.setattr(utils, 'requests', TestingFiles())
