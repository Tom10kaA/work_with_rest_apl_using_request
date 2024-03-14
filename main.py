from star_wars_api import StarWarsApi
api_client = StarWarsApi()

person = api_client.get_person(1)
print(f'Person name: {person.name}')
print(f'Person skin_color: {person.skin_color}')


api_client = StarWarsApi()

planets = api_client.get_planet(3)
print(f'Planets name: {planets.name}')
