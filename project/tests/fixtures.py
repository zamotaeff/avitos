import pytest
from datetime import timedelta

from django.utils import timezone


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    username = 'test_user'
    password = 'testpass'
    birth_date = timezone.now() - timedelta(days=500)
    django_user_model.objects.create_user(username=username,
                                          password=password,
                                          birth_date=birth_date,
                                          role='admin')

    response = client.post("/user/token/",
                           {"username": username,
                            "password": password},
                           content_type="application/json")
    print(response.data)
    return response.data['access']
