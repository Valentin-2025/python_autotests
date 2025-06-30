import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b373a8c818441535a76ad73f87e245bb'
HEADER = {'Content-Type':'application/json' , 'trainer_token':TOKEN}
TRAINER_ID = '36237'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', headers=HEADER)
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Кот обормот'

@pytest.mark.parametrize('key, value', [('trainer_name', 'Кот обормот'), ('trainer_id', TRAINER_ID), ('id', '36237')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url=f'{URL}/trainers', headers=HEADER, params={'trainer_id': TRAINER_ID})
    assert response_parametrize.json()
