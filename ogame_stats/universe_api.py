#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:16:05 2019
@author: kan

Update frequencies:

    players.xml -> daily
    universe.xml -> weekly
    highscore.xml -> hourly
    alliances.xml -> daily
    serverData.xml -> daily
    playerData.xml -> weekly
    localization.xml -> static
    universes.xml -> static

"""
import json
import pandas as pd
from typing import Union, Dict
from urllib.parse import urlencode
from .utils import ApiBaseClass


class UniverseDataUrls(ApiBaseClass):
    def __init__(self, universe_id: int, community: str):
        self.universe_id = universe_id
        self.community = community

    def _get_base_url(self) -> str:
        return f"https://s{self.universe_id}-{self.community}.ogame.gameforge.com/api"

    def _get_serverdata_url(self) -> str:
        return f"{self._get_base_url()}/serverData.xml"

    def _get_universe_url(self) -> str:
        return f"{self._get_base_url()}/universe.xml"

    def _get_players_url(self) -> str:
        return f"{self._get_base_url()}/players.xml"

    def _get_alliances_url(self) -> str:
        return f"{self._get_base_url()}/alliances.xml"

    def _get_localization_url(self) -> str:
        return f"{self._get_base_url()}/localization.xml"

    def _get_playerdata_url(self, player_id: int) -> str:
        query = {'id': player_id}
        return f'{self._get_base_url()}/playerData.xml?{urlencode(query)}'

    def load_server_data(self) -> {str: str}:
        url = self._get_serverdata_url()
        return self._load_kv_style_data(url)

    def load_players_data(self) -> pd.DataFrame:
        """['id', 'name', 'status', 'alliance']"""
        url = self._get_players_url()
        return self._load_data_as_df(url)

    def load_universe_data(self) -> pd.DataFrame:
        """['id', 'player', 'name', 'coords']"""
        url = self._get_universe_url()
        return self._load_data_as_df(url)

    def load_alliances_data(self) -> pd.DataFrame:
        """['foundDate', 'founder', 'homepage', 'id', 'logo', 'name', 'open', 'tag']"""
        url = self._get_alliances_url()
        return self._load_data_as_df(url)

    def load_localization_data(self) -> Dict:
        """{'techs': {'1': 'Metal Mine'}, 'missions': {'1': 'Attack'}"""
        url = self._get_localization_url()
        return self._load_nested_data(url)

    def load_player_data(self, player_id: Union[int, str]) -> Dict:
        url = self._get_playerdata_url(player_id)
        return self._load_data_via_xmltodict(url)


class UniverseData:
    players: pd.DataFrame = None
    universe: pd.DataFrame = None
    alliances: pd.DataFrame = None
    serverdata: dict = None
    techs: dict = None
    missions: dict = None
    universe_id: int = None
    community: str = None
    urls: UniverseDataUrls = None

    def __init__(self, universe_id: int, community: str):
        """
        Args:
            universe_id (int): an integer identifying the universe (e.g. 162 - Janice)
            community (str):  an string indicating (language) community='en'
        """
        self.universe_id = universe_id
        self.community = community
        self.urls = UniverseDataUrls(universe_id, community)
        self.players = self.urls.load_players_data()
        self.universe = self.urls.load_universe_data()
        self.universe_coords_list = self.universe['coords'].to_list()
        self.alliances = self.urls.load_alliances_data()
        self.serverdata = self.urls.load_server_data()
        localization = self.urls.load_localization_data()
        self.techs = localization['techs']
        self.missions = localization['missions']


class UniverseQuestions(UniverseData):
    def __init__(self, universe_id: int, community: str):
        """
        Args:
            universe_id (int): an integer identifying the universe (e.g. 162 - Janice)
            community (str):  an string indicating (language) community='en'
        """
        super().__init__(universe_id, community)

    def get_planets_of_player(self, player_name: str) -> dict:
        player_id_str = self.get_player_id(player_name)
        results = self.universe.query('player == @player_id_str')
        results = results.reset_index(drop=True)
        return results[['coords', 'name']].to_dict(orient='records')

    def get_planets_of_player_by_id(self, player_id_str: str) -> dict:
        results = self.universe.query('player == @player_id_str')
        results = results.reset_index(drop=True)
        return results[['coords', 'name']].to_dict(orient='records')

    def get_planets_of_player_as_json(self, player_name: str):
        results = self.get_planets_of_player(player_name)
        return json.dumps(results, indent=2)

    def get_player_id(self, player_name: str) -> str:
        try:
            return str(self.players.query('name == @player_name').iloc[0]['id'])
        except IndexError:
            print(f"`{player_name}` not found. look at `players['name']` for valid player names")

    def get_player_status(self, player_name: str) -> str:
        """['a', nan, 'vi', 'v', 'I', 'vIb', 'vb', 'vI', 'i', 'o', 'vib', 'vo']"""
        return str(self.players.query("name == @player_name").iloc[0]['status'])

    def get_player_alliance(self, player_name: str) -> str:
        """integer as str"""
        return str(self.players.query("name == @player_name").iloc[0]['alliance'])

    def get_player_data(self, player_name: str) -> dict:
        player_id_str = self.get_player_id(player_name)
        return self.urls.load_player_data(player_id_str)

    def get_player_data_as_json(self, player_name: str) -> str:
        return json.dumps(self.get_player_data(player_name), indent=2)

    def get_alliance_id_by_tag(self, tag: str) -> str:
        return self.alliances.query('tag == @tag').iloc[0]['id']

    def get_alliance_id_by_name(self, name: str) -> str:
        return self.alliances.query('name == @name').iloc[0]['id']

    def get_players_of_alliance(self, tag: str) -> pd.DataFrame:
        alliance_id = self.get_alliance_id_by_tag(tag)
        members = self.players.query('alliance == @alliance_id')
        return members

    def get_players_of_alliances_by_name(self, name: str) -> pd.DataFrame:
        alliance_id = self.get_alliance_id_by_name(name)
        members = self.players.query('alliance == @alliance_id')
        return members

    def get_planets_of_alliance(self, tag: str) -> [str]:
        members = self.get_players_of_alliance(tag)
        member_ids = members['id'].to_list()
        data = [self.get_planets_of_player_by_id(player_id) for player_id in member_ids]
        coords = [planet['coords'] for player in data for planet in player]
        coords.sort()
        return coords

    def get_planets_distribution_by_galaxy(self, alliance_tag: str) -> Dict:
        galaxy_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        coords = self.get_planets_of_alliance(alliance_tag)
        return {galaxy: sum([elm[0] == galaxy for elm in coords]) for galaxy in galaxy_list}

    def is_planet_taken(self, coords_str: str) -> bool:
        if coords_str in self.universe_coords_list:
            result = True
        else:
            result = False
        return result
