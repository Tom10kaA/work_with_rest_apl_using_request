import requests

from entity.person import Person
from entity.planets import Planets


class StarWarsApi:
    def __init__(self):
        self.base_url = 'https://swapi.dev/'

    def get_entity(self, entity, entity_id):
        url = f'{self.base_url}/api/{entity}/{entity_id}/'
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError(f'не можливо отримати дані для сутності {entity} з індифікатором {entity_id} ')

    def get_person(self, person_id):
        person_dict = self.get_entity('people', person_id)
        return Person(person_dict)

    def get_planet(self, planet_id):
        planets_dict = self.get_entity('planets', planet_id)
        return Planets(planets_dict)
