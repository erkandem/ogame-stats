import pytest
from ogame_stats.universes_api import UniversesDataUrls
from ogame_stats import UniversesData
from ogame_stats import UniversesQuestions
from .testing_utils import Constants
from .testing_utils import mock_requests


class TestUniversesDataUrls(Constants):
    def test__get_universes_url(self):
        udu = UniversesDataUrls()
        expected = 'https://lobby.ogame.gameforge.com/api/servers'
        result = udu._get_universes_url()
        assert result == expected


class TestUniversesData:
    def test__init__(self, mock_requests):
        hs = UniversesData()


class TestUniversesQuestions:
    def test__init__(self, mock_requests):
        q = UniversesQuestions()
