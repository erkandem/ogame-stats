## ogame stats

wrapper and logic around public game statistics for https://ogame.org

---

Some classes and methods to retrieve public data of the online game `ogame`.
This package is **NOT** intended to interact with an account - which is forbidden anyway.

Might be used to query the data sets, visualize results and generally to do data analysis.

## requirements
depends on:
 - python >= 3.6 (uses f-string)
 - xmltodict as a convenience to convert XML data to more basic python types
 - requests to perform http requests and
 - pandas to perform queries on the data


## installation
create your virtualenv with your preferred versionin a new directory
```
virtualenv -p python3.<6,7,8> venv
```

install the wrapper
```
pip install ogama_stats
```

## usage

### basic usage
the most basic usage would look like.
```python
#%%
import ogame_stats

#%% supply the two inputs to uniquely identify a universe
universe_id = 162
community = 'en'

#%% instantiate and thereby load the data
universe = ogame_stats.UniverseQuestions(universe_id, community)
```

than you could take a look at the data sets.

```python
#%% get a list of all the planets
universe.universe
            id  player          name    coords
0            1       1        Arakis     1:1:2
...        ...     ...           ...       ...
[4378 rows x 4 columns]

#%% find some players
universe.players
         id              name status alliance
0         1             Legor      a      NaN
..      ...               ...    ...      ...
[751 rows x 4 columns]
```

## advanced usage
Now, data itself is nice. But lets ask it some questions. 
**This is needs your help since asking the right questions is the key.**

e.g. look up the planets of a user.

```python
##%% get the coordinates and names of all the planets of a player
universe.get_planets_of_player('someSpecialName')
[{'coords': '1:45:4', 'name': 'MotherPlanet'},
{'coords': '1:144:2', 'name': 'ColonyC'},
{'coords': '1:145:3', 'name': 'ColonyB'},
{'coords': '1:303:5', 'name': 'ColonyA'}, 
{'coords': '5:119:9', 'name': 'ColonyE'}, 
{'coords': '1:289:9', 'name': 'ColonyD'},
{'coords': '1:389:9', 'name': 'ColonyF'}]
```

or ask for the status (active, inactive, banned, holiday etc.). 
```python
universe.get_player_status('someSpecialName')
'I'
```

or just dump everything about `someSpecialName`:
```python
universe.get_player_data('someSpecialName')
```

get the complete list of players within a specific alliance
```python
universe.get_players_of_alliance('someAlliance')
         id                 name status alliance
291  103910           reabuilder    NaN   500234
292  103930              1 4 Fun      v   500234
312  104181            night owl    NaN   500234
...
```

get to see the distribution of the planets owned by the alliance members.
```python
universe.get_planets_distribution_by_galaxy('someAlliance')
{'1': 7, '2': 17, '3': 29, '4': 38, '5': 9, '6': 9, '7': 9, '8': 2, '9': 6} 
```


### Update frequencies of data
Don't spam the servers with requests. Since the data sets and classes avoid the usage of 
XML attributes, it's easy to just pickle your `UniverseData` for tests, development and everything else. 
These are the update frequencies I copied over at some point in time (might have changed):

```
players.xml -> daily
universe.xml -> weekly
highscore.xml -> hourly
alliances.xml -> daily
serverData.xml -> daily
playerData.xml -> weekly
localization.xml -> static
universes.xml -> static
```

Maybe the easiest way would be to use [requests_cache](https://github.com/reclosedev/requests-cache).

```
import requests_cache
requests_cache.install_cache('demo_cache')
```

## issues/ideas
 ... are generally welcome. saves us time.
Also, the overall design is far from being ideal.
Pull requests welcome. Be sure to include the tests.
