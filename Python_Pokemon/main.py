import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'Token_user'
HEADER = {'Content-Type': 'application/json' , 'trainer_token' : TOKEN}

'''# Верификация, идентификация, ауторизация, валидация
body_registration = {
    "trainer_token": TOKEN,
    "email": "USER_LOGIN",
    "password": "USER_PASSWORD"
}

body_confirmation = {
    "trainer_token": TOKEN
}'''


# 1. Создаём покемона:
body_create = {
    "name": "Бульбазавр",
    "photo_id": 12
}
   
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.status_code)
print(response_create.json())

# 2. Сохраняем ID покемона:
if response_create.status_code == 201:
    response_data = response_create.json()
    pokemon_id = response_data['id']
    print(f"ID созданного покемона: {pokemon_id}")

# 3. Ловим покемона в покебол:
body_catch = {
    "pokemon_id": pokemon_id
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.status_code)
print(response_catch.json())

# 4. Смена имени покемона 
body_name = {
    "pokemon_id": pokemon_id,
    "name": "Валидол",
    "photo_id": 12  
}

response_name = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_name)
print(response_name.status_code)
print(response_name.json())

# 5. Запрашиваем информацию о покемоне
response_info = requests.get(f'{URL}/pokemons/{pokemon_id}', headers=HEADER)
print("\nЗапрос информации о покемоне:")
pokemon_info = response_info.json()
print(f"Полный ответ: {response_info.json()}")

''' response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

