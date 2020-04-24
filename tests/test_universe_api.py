from ogame_stats.universe_api import UniverseDataUrls
from .testing_utils import Constants


class TestUniverseDataUrls(Constants):
    def test__get_base_path(self):
        udu = UniverseDataUrls(self.universe_id, self.community)
        expected = f"https://s{self.universe_id}-{self.community}.ogame.gameforge.com/api"
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

class TestUniverseData:
    pass
