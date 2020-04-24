from pathlib import Path
import zipfile


class TestingFiles:
    ARCHIVE_FILEPATH = Path('tests/testing_data/testing_data.zip')
    file_mapping = {
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
    }

    def get_file_path(self, file_type: str):
        if file_type not in self.file_mapping.keys():
            raise KeyError(
                f'got `{file_type}`. valid ones are {list(self.file_mapping)}.'
            )
        return self.file_mapping[file_type]

    def load_file(self, file_type: str) -> bytes:
        with zipfile.ZipFile(self.ARCHIVE_FILEPATH, 'r') as zf:
            file_name = self.get_file_path(file_type)
            data = zf.read(file_name)
        return data

    def load_file_as_str(self, file_type: str) -> str:
        return self.load_file(file_type).decode()
