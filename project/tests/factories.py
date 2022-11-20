from datetime import date, timedelta, datetime

import factory
from django.utils import timezone

from ads.models import Category, Ad
from users.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')
    slug = factory.Faker('ean', length=8)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    password = factory.Faker('password')
    role = 'admin'
    age = 43
    birth_date = timezone.now() - timedelta(days=500)


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = factory.Faker('name')
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    price = 1400
    description = ""
    is_published = True

