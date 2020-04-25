import pytest
from ogame_stats.universe_api import UniverseDataUrls
from ogame_stats import UniverseData
from ogame_stats import UniverseQuestions
from .testing_utils import Constants
from .testing_utils import mock_requests


class TestUniverseDataUrls(Constants):
    def test__get_base_path(self):
        udu = UniverseDataUrls(self.universe_id, self.community)
        expected = (
            f"https://s{self.universe_id}-{self.community}.ogame.gameforge.com/api"
        )
        result = udu._get_base_url()
        assert result == expected

    def test__get_serverdata_url(self):
        udu = UniverseDataUrls(self.universe_id, self.community)
        expected = f"{udu._get_base_url()}/serverData.xml"
        result = udu._get_serverdata_url()
        assert result == expected

    def test__get_universe_url(self):
        udu = UniverseDataUrls(self.universe_id, self.community)
        expected = f"{udu._get_base_url()}/universe.xml"
        result = udu._get_universe_url()
        assert result == expected

    def test__get_players_url(self):
        udu = UniverseDataUrls(self.universe_id, self.community)
        expected = f"{udu._get_base_url()}/players.xml"
        result = udu._get_players_url()
        assert result == expected

    def test__get_alliances_url(self):
        udu = UniverseDataUrls(self.universe_id, self.community)
        expected = f"{udu._get_base_url()}/alliances.xml"
        result = udu._get_alliances_url()
        assert result == expected

    def test__get_localization_url(self):
        udu = UniverseDataUrls(self.universe_id, self.community)
        expected = f"{udu._get_base_url()}/localization.xml"
        result = udu._get_localization_url()
        assert result == expected

    def test__get_playerdata_url(self):
        udu = UniverseDataUrls(self.universe_id, self.community)
        expected = f"{udu._get_base_url()}/playerData.xml?id=1"
        result = udu._get_playerdata_url(1)
        assert result == expected


class TestUniverseDataUrlsAccessingData(Constants):
    def test_load_player_data(self):
        udu = UniverseDataUrls(self.universe_id, self.community)
        data = udu.load_player_data(110008)


class TestUniverseData(Constants):
    def test_that_it_is_patched(self, mock_requests):
        """depends on the sample data which contains only data for universe 162"""
        with pytest.raises(KeyError):
            hs = UniverseData(361, 'en')

    def test_get_total_data(self, mock_requests):
        universe = UniverseData(self.universe_id, self.community)


class TestUniverseQuestions(Constants):
    def test_get_total_data(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
