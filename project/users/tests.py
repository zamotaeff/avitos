import json
from unittest import TestCase

import requests
from faker import Faker

HOST = 'http://127.0.0.1:8000'
fake = Faker(['en-US'])


class UserClassTestCase(TestCase):

    def test_detail(self):
        response = requests.get(f'{HOST}/user/10/', timeout=5)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('id'), 10)

    def test_detail_pagination(self):
        response = requests.get(f'{HOST}/user/?page=1', timeout=5)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json().get('items', 0)), 5)
        print('Items on page', len(response.json().get('items', 0)))

    def test_list(self):
        response = requests.get(f'{HOST}/user/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json().get('items', 0)), 0)
        print('Items on page')

    def test_create(self):
        post_data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "username": fake.profile().get('username'),
            "password": "password",
            "role": "admin",
            "age": 42,
            "location": ["Москва", "Владимир"]
        }

        response = requests.post(f'{HOST}/user/create/',
                                 data=json.dumps(post_data),
                                 timeout=5)

        if 300 > response.status_code >= 200:
            print('Status code', response.status_code)

            self.assertEqual(response.json().get('first_name'),
                             post_data['first_name'])
            print('Create user with id', response.json().get('id'))
            print(response.json())
            return response.json().get('id')
        else:
            print('Error create user')

    def test_update(self):
        user_id = self.test_create()

        user = {
            "first_name": fake.name(),
            "last_name": fake.name(),
            "password": "password",
            "price": 1200,
            "description": "ad.description",
            "is_published": True,
            "location": ["Ереван", "ул. Маяковского 17"]
        }
        response = requests.post(f'{HOST}/user/{user_id}/update/',
                                 data=json.dumps(user),
                                 timeout=15)
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        user_id = self.test_create()
        response = requests.post(f'{HOST}/user/{user_id}/delete/', timeout=10)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('status'), 'ok')
