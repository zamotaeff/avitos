import json

from django.conf import settings
from django.core.management import BaseCommand

from ads.models import Ad


class Command(BaseCommand):
    help = 'Add new object from json files'

    # TODO: pass file names in parameters

    def handle(self, *args, **kwargs):
        with open(settings.FILE_JSON_ADS, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

            for item in json_data:
                new_ads = Ad(
                    name=item.get('name'),
                    author_id=item.get('author_id'),
                    price=item.get('price'),
                    description=item.get('description'),
                    is_published=bool(item.get('is_published')),
                    image=item.get('image'),
                    category_id=item.get('category_id')
                )
                new_ads.save()
