from django.core.management.base import BaseCommand

from ads.helpers import (convert_csv_to_json,
                         FILE_CSV_LOCATIONS,
                         FILE_CSV_USERS,
                         FILE_JSON_LOCATIONS,
                         FILE_JSON_USERS)


class Command(BaseCommand):
    help = 'Create json from csv files'

    # TODO: pass file names in parameters

    def handle(self, *args, **kwargs):

        convert_csv_to_json(FILE_CSV_LOCATIONS, FILE_JSON_LOCATIONS)

        convert_csv_to_json(FILE_CSV_USERS, FILE_JSON_USERS)
