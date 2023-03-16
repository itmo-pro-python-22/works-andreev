from typing import Union, Generator
import requests
from functools import lru_cache
from dataclasses import dataclass


class BasePokemon:
    _name: str

    def __init__(self, name: str) -> None:
        self._name = name

    def __str__(self) -> str:
        return f'BasePokemon(name={self._name})'

    @property
    def name(self):
        return self._name

    # def get_name(self) -> str:
    #     return self.__name


class Pokemon(BasePokemon):
    __pokemon_id: int
    __height: int
    __weight: int

    def __init__(self, pokemon_id: int, name: str, height: int, weight: int):
        super().__init__(name)
        self.__pokemon_id = pokemon_id
        self.__height = height
        self.__weight = weight

    def __str__(self) -> str:
        return f'Pokemon(pokemon_id={self.__pokemon_id}, name={self._name}, height={self.__height} decimeters, weight={self.__weight} hectograms)'

    def get_id(self) -> int:
        return self.__pokemon_id

    def get_height(self) -> int:
        return self.__height

    def get_weight(self) -> int:
        return self.__weight


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











