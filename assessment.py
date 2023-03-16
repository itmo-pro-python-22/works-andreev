from typing import Union, Generator
import requests
from functools import lru_cache
from dataclasses import dataclass


@dataclass(frozen=True)
class BasePokemon:
    name: str


@dataclass(frozen=True)
class Pokemon(BasePokemon):
    pokemon_id: int
    height: int
    weight: int


class PokeAPI:
    @staticmethod
    @lru_cache
    def get_pokemon(name: Union[int, str]) -> Pokemon:
        url: str = f'https://pokeapi.co/api/v2/pokemon/{name}'
        data: dict = requests.get(url).json()
        pokemon: Pokemon = Pokemon(pokemon_id=data['id'],
                          name=data['name'],
                          weight=data['weight'],
                          height=data['height'])
        return pokemon

    @staticmethod
    def get_all(get_full=False) -> Generator:
        url: str = 'https://pokeapi.co/api/v2/pokemon/'
        data: dict = requests.get(url).json()
        while True:
            for pokemon in data['results']:
                if get_full:
                    yield PokeAPI.get_pokemon(pokemon['name'])
                else:
                    yield BasePokemon(name=pokemon['name'])
            if data['next'] is None:
                break
            url = data['next']
            data = requests.get(url).json()


# for pokemon in PokeAPI.get_all(True):
#     print(pokemon)

for i in range(50):
    pikachu: Pokemon = PokeAPI.get_pokemon('pikachu')
    print(pikachu)











