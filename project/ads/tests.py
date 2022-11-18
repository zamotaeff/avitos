import json
from unittest import TestCase

import requests
from faker import Faker

HOST = 'http://127.0.0.1:8000'
fake = Faker()


class CategoryClassTestCase(TestCase):

    def test_detail(self):
        cat_id = self.test_create()
        if cat_id:
            response = requests.get(f'{HOST}/cat/{cat_id}/', timeout=5)
            self.assertEqual(response.status_code, 200)

    def test_list(self):
        response = requests.get(f'{HOST}/cat/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json()), 0)
        print('Items on page')

    def test_create(self):
        post_data = {
            "name": "New category" + str(fake.random.randint(0, 10))
        }
        response = requests.post(f'{HOST}/cat/create/',
                                 data=json.dumps(post_data),
                                 timeout=10)

        if 300 > response.status_code >= 200:
            print('Status code', response.status_code)

            self.assertEqual(response.json().get('name'), post_data['name'])
            print('Create category with id', response.json().get('id'))

            return response.json().get('id')

    def test_delete(self):
        cat_id = self.test_create()
        if cat_id:
            response = requests.post(f'{HOST}/cat/{cat_id}/delete/', timeout=10)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json().get('status'), 'ok')

    def test_update(self):
        cat_id = self.test_create()
        if cat_id:
            cat = {
                "name": fake.word()
            }
            response = requests.post(f'{HOST}/cat/{cat_id}/update/',
                                     data=json.dumps(cat),
                                     timeout=10)
            self.assertEqual(response.status_code, 200)


class AdClassTestCase(TestCase):

    def test_detail(self):
        response = requests.get(f'{HOST}/ad/10/', timeout=5)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('id'), 10)

    def test_detail_pagination(self):
        response = requests.get(f'{HOST}/ad/?page=1', timeout=5)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json().get('items', 0)), 5)
        print('Items on page', len(response.json().get('items', 0)))

    def test_list(self):
        response = requests.get(f'{HOST}/ad/')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(response.json().get('items', 0)), 0)
        print('Items on page')

    def test_create(self):

        post_data = {
            "name": fake.job(),
            "author_id": 3,
            "category_id": 1,
            "price": fake.pricetag(),
            "description": fake.paragraph(nb_sentences=1),
            "is_published": True
        }
        response = requests.post(f'{HOST}/ad/create/', data=json.dumps(post_data), timeout=5)

        if 300 > response.status_code >= 200:
            print('Status code', response.status_code)

            self.assertEqual(response.json().get('name'), post_data['name'])
            print('Create ad with id', response.json().get('id'))

            return response.json().get('id')

    def test_delete(self):
        ad_id = self.test_create()
        if ad_id:
            response = requests.post(f'{HOST}/ad/{ad_id}/delete/', timeout=10)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json().get('status'), 'ok')

    def test_update(self):
        ad_id = self.test_create()
        if ad_id:
            ad = {
                "name": "test name",
                "author_id": 3,
                "category_id": 1,
                "price": 1200,
                "description": "ad.description",
                "is_published": True
            }
            response = requests.post(f'{HOST}/ad/{ad_id}/update/',
                                     data=json.dumps(ad),
                                     timeout=15)
            self.assertEqual(response.status_code, 200)
