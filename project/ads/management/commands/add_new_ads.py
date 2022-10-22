import json

from django.core.management import BaseCommand

from ads.models import Ad, Category
from users.models import User
from ads.helpers import FILE_JSON_ADS


class Command(BaseCommand):
    help = 'Add new object from json files'

    # TODO: pass file names in parameters

    def handle(self, *args, **kwargs):
        with open(FILE_JSON_ADS, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

            for item in json_data:

                ad_author = User.objects.get(item.get('author_id'))
                ad_category = Category.objects.get(item.get('category_id'))

                new_ads = Ad(
                    name=item.get('name'),
                    author=ad_author,
                    price=item.get('price'),
                    description=item.get('description'),
                    is_published=bool(item.get('is_published')),
                    image=item.get('image'),
                    category=ad_category
                )
                new_ads.save()
