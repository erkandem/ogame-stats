import pytest
from numpy import nan
import pandas as pd
from ogame_stats.universe_api import UniverseDataUrls
from ogame_stats import UniverseData
from ogame_stats import UniverseQuestions
from .testing_utils import Constants
from .testing_utils import mock_requests


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


class TestUniverseData(Constants):
    def test_that_it_is_patched(self, mock_requests):
        """depends on the sample data which contains only data for universe 162"""
        with pytest.raises(KeyError):
            hs = UniverseData(361, "en")

    def test_get_total_data(self, mock_requests):
        universe = UniverseData(self.universe_id, self.community)


class TestUniverseQuestions(Constants):
    player_name = "Senator Thrust"
    play_id = "105178"
    planets = [
        {"name": "Colony", "coords": "3:54:6"},
        {"name": "Colony", "coords": "3:54:14"},
        {"name": "Colony", "coords": "3:54:15"},
        {"name": "Colony", "coords": "3:54:1"},
        {"name": "Colony", "coords": "4:288:8"},
        {"name": "Colony", "coords": "2:436:9"},
    ]

    def test_get_player_id(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        result = q.get_player_id(self.player_name)
        assert result == self.play_id

    def test_get_player_id_fails(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        with pytest.raises(IndexError):
            q.get_player_id(self.player_name + "suffix")

    def test_get_planets_of_player(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        result = q.get_planets_of_player(self.player_name)
        assert result == self.planets

    def test_get_planets_of_player_by_id(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        result = q.get_planets_of_player_by_id(self.play_id)
        assert result == self.planets

    def test_get_planets_of_player_as_json(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        result = q.get_planets_of_player_as_json(self.player_name)
        expected = (
            '[{"coords": "3:54:6", "name": "Colony"},'
            ' {"coords": "3:54:14", "name": "Colony"},'
            ' {"coords": "3:54:15", "name": "Colony"},'
            ' {"coords": "3:54:1", "name": "Colony"},'
            ' {"coords": "4:288:8", "name": "Colony"},'
            ' {"coords": "2:436:9", "name": "Colony"}]'
        )
        assert result == expected

    def test_get_player_status(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        result = q.get_player_status(self.player_name)
        expected = "vI"
        assert result == expected


class TestPlayerData(Constants):
    player_name = "TS X0X0"
    player_id = "110008"
    alliance_id = "500234"
    alliance_tag = "Amitabha"
    alliance_name = "NamoAmitabha"
    alliance_members = [
        {"id": "103910", "name": "reabuilder", "status": nan, "alliance": "500234"},
        {"id": "103930", "name": "1 4 Fun", "status": "v", "alliance": "500234"},
        {"id": "104181", "name": "night owl", "status": nan, "alliance": "500234"},
        {"id": "105102", "name": "0rb1337", "status": nan, "alliance": "500234"},
        {"id": "105226", "name": "tsintsouli", "status": "vI", "alliance": "500234",},
        {"id": "105860", "name": "Faithslayer", "status": "vI", "alliance": "500234",},
        {"id": "105882", "name": "Stadtholder Deimos", "status": "vI", "alliance": "500234",},
        {"id": "105887", "name": "MrBugs3k", "status": "I", "alliance": "500234"},
        {"id": "105991", "name": "Wrath", "status": nan, "alliance": "500234"},
        {"id": "106229", "name": "Deviant601", "status": "vI", "alliance": "500234",},
        {"id": "107462", "name": "Consul Saros", "status": "vi", "alliance": "500234",},
        {"id": "108073", "name": "Vice Astra", "status": nan, "alliance": "500234"},
        {"id": "108078", "name": "L33tmandude", "status": "vI", "alliance": "500234",},
        {"id": "108232", "name": "Procurator Xanthus", "status": nan, "alliance": "500234",},
        {"id": "108506", "name": "Robis of Windy Hill", "status": "v", "alliance": "500234",},
        {"id": "108679", "name": "hooter", "status": "vi", "alliance": "500234"},
        {"id": "108694", "name": "sexy mel", "status": "vI", "alliance": "500234"},
        {"id": "108704", "name": "Looney", "status": "vI", "alliance": "500234"},
        {"id": "108713", "name": "Everglade", "status": "v", "alliance": "500234"},
        {"id": "108779", "name": "CAPTAIN JANEWAY", "status": "v", "alliance": "500234",},
        {"id": "108809", "name": "Commodore Elara", "status": nan, "alliance": "500234",},
        {"id": "110008", "name": "TS X0X0", "status": nan, "alliance": "500234"},
        {"id": "110103", "name": "BLITZ", "status": nan, "alliance": "500234"},
    ]

    def test_get_player_data(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        result = q.get_player_data(self.player_name)
        expected = {
            "playerData": {
                "id": "110008",
                "name": "TS X0X0",
                "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
                "xsi:noNamespaceSchemaLocation": "https://s162-en.ogame.gameforge.com/api/xsd/playerData.xsd",
                "timestamp": "1587724187",
                "serverId": "en162",
                "positions": {
                    "position": [
                        {"type": "0", "score": "1806", "#text": "585"},
                        {"type": "1", "score": "1465", "#text": "582"},
                        {"type": "2", "score": "214", "#text": "595"},
                        {"type": "3", "score": "160", "ships": "28", "#text": "536"},
                        {"type": "4", "score": "0", "#text": "626"},
                        {"type": "5", "score": "160", "#text": "596"},
                        {"type": "6", "score": "36", "#text": "571"},
                        {"type": "7", "score": "0", "#text": "555"},
                    ]
                },
                "planets": {"planet": {"id": "33749193", "name": "hangry", "coords": "5:215:6"}},
                "alliance": {"id": "500234", "name": "NamoAmitabha", "tag": "Amitabha"},
            }
        }
        assert result == expected

    def test_get_player_data_as_json(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        result = q.get_player_data_as_json(self.player_name)
        expected = (
            '{"playerData": {"id": "110008", "name": "TS X0X0", '
            '"xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance", '
            '"xsi:noNamespaceSchemaLocation": "https://s162-en.ogame.gameforge.com/api/xsd/playerData.xsd", '
            '"timestamp": "1587724187", "serverId": "en162", "positions": '
            '{"position": ['
            '{"type": "0", "score": "1806", "#text": "585"}, '
            '{"type": "1", "score": "1465", "#text": "582"}, '
            '{"type": "2", "score": "214", "#text": "595"}, '
            '{"type": "3", "score": "160", "ships": "28", "#text": "536"}, '
            '{"type": "4", "score": "0", "#text": "626"}, '
            '{"type": "5", "score": "160", "#text": "596"}, '
            '{"type": "6", "score": "36", "#text": "571"}, '
            '{"type": "7", "score": "0", "#text": "555"}]}, '
            '"planets": {"planet": {"id": "33749193", "name": "hangry", "coords": "5:215:6"}}, '
            '"alliance": {"id": "500234", "name": "NamoAmitabha", "tag": "Amitabha"}}}'
        )
        assert result == expected

    def test_get_alliance_id_by_tag(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        result = q.get_alliance_id_by_tag(self.alliance_tag)
        assert result == self.alliance_id

    def test_get_alliance_id_by_name(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        result = q.get_alliance_id_by_name(self.alliance_name)
        assert result == self.alliance_id

    def test_get_players_of_alliance(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        result = q.get_players_of_alliance(self.alliance_tag)
        result = result.to_dict(orient="records")
        assert result == self.alliance_members

    def test_get_players_of_alliances_by_name(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        result = q.get_players_of_alliances_by_name(self.alliance_name)
        result = result.to_dict(orient="records")
        assert result == self.alliance_members

    def test_get_player_alliance(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        result = q.get_player_alliance(self.player_name)
        assert result == self.alliance_id

    def test_is_planet_taken(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        result = q.is_planet_taken("3:54:6")
        assert result is True

    def test_is_planet_taken_fails(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        result = q.is_planet_taken("3:54:4")
        assert result is False

    def test_get_planets_of_alliance(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        results = q.get_planets_of_alliance("Amitabha")
        expected = [
            "1:125:5", "1:178:8", "1:193:10", "1:214:7", "1:359:9", "1:375:4", "1:60:8", "2:125:12",
            "2:159:4", "2:178:8", "2:285:11", "2:285:12", "2:289:12", "2:310:8", "2:317:8", "2:319:6",
            "2:340:7", "2:341:6", "2:342:7", "2:355:8", "2:35:4", "2:361:8", "2:375:12", "2:81:8",
            "3:102:4", "3:13:9", "3:213:10", "3:213:11", "3:213:12", "3:213:14", "3:213:15", "3:213:9",
            "3:214:10", "3:214:11", "3:231:6", "3:239:11", "3:239:12", "3:239:13", "3:239:14",
            "3:239:15", "3:239:4", "3:239:5", "3:239:6", "3:239:7", "3:265:4", "3:295:12", "3:300:11",
            "3:317:9", "3:36:8", "3:374:8", "3:378:8", "3:65:4", "3:82:8", "4:125:5", "4:13:9",
            "4:159:8", "4:214:13", "4:214:7", "4:214:9", "4:219:10", "4:219:11", "4:219:12",
            "4:219:15", "4:219:5", "4:220:10", "4:220:11", "4:220:12", "4:220:8", "4:220:9", "4:221:7",
            "4:226:11", "4:23:9", "4:262:10", "4:262:12", "4:262:7", "4:262:9", "4:289:7", "4:327:12",
            "4:341:8", "4:342:8", "4:374:4", "4:378:6", "4:382:8", "4:398:12", "4:407:4", "4:407:5",
            "4:407:7", "4:449:8", "4:63:9", "4:78:6", "4:99:4", "5:135:8", "5:135:9", "5:13:9",
            "5:214:7", "5:215:6", "5:235:8", "5:238:12", "5:270:9", "5:95:8", "6:13:9", "6:278:1",
            "6:278:15", "6:280:10", "6:280:6", "6:280:9", "6:281:7", "6:289:7", "6:378:8", "7:13:9",
            "7:236:8", "7:246:8", "7:257:1", "7:257:8", "7:285:4", "7:285:5", "7:335:8", "7:380:8",
            "8:168:8", "8:301:8", "9:252:8", "9:267:8", "9:285:7", "9:285:8", "9:285:9", "9:399:1"
        ]
        assert results == expected

    def test_get_planets_distribution_by_galaxy(self, mock_requests):
        q = UniverseQuestions(self.universe_id, self.community)
        results = q.get_planets_distribution_by_galaxy("Amitabha")
        expected = {"1": 7, "2": 17, "3": 29, "4": 38, "5": 9, "6": 9, "7": 9, "8": 2, "9": 6}
        assert results == expected
