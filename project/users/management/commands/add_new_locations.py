import json

from django.core.management import BaseCommand

from users.models import Location
from ads.helpers import FILE_JSON_LOCATIONS


class Command(BaseCommand):
    help = 'Add new object from json files'

    # TODO: pass file names in parameters

    def handle(self, *args, **kwargs):

        with open(FILE_JSON_LOCATIONS, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

            for item in json_data:
                new_location = Location(
                    name=item.get('name'),
                    lat=item.get('lat'),
                    lng=item.get('lng')
                )
                new_location.save()
