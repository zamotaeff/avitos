import json

from django.core.management import BaseCommand

from users.models import Location, User
from ads.helpers import FILE_JSON_USERS


class Command(BaseCommand):
    help = 'Add new object from json files'

    # TODO: pass file names in parameters

    def handle(self, *args, **kwargs):
        with open(FILE_JSON_USERS, 'r', encoding='utf-8') as file:
            json_data = json.load(file)

            for item in json_data:

                user_location = Location.objects.get(item.get('location_id'))

                new_user = User(
                    first_name=item.get('first_name'),
                    last_name=item.get('last_name'),
                    username=item.get('username'),
                    password=item.get('password'),
                    role=item.get('role'),
                    age=item.get('age'),
                    location=user_location
                )
                new_user.save()
