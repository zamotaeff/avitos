import json

from django.core.management import BaseCommand

from ads.models import Category
from ads.helpers import FILE_JSON_CATEGORIES


class Command(BaseCommand):
    help = 'Add new object from json files'

    # TODO: pass file names in parameters

    def handle(self, *args, **kwargs):

        with open(FILE_JSON_CATEGORIES, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

            for item in json_data:
                new_category = Category(
                    name=item.get('name')
                )
                new_category.save()
