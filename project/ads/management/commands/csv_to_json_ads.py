from avito.settings import (FILE_CSV_ADS,
                            FILE_JSON_ADS,
                            FILE_CSV_CATEGORIES,
                            FILE_JSON_CATEGORIES)
from django.core.management.base import BaseCommand

from ads.helpers import convert_csv_to_json


class Command(BaseCommand):
    help = 'Create json from csv files'

    # TODO: pass file names in parameters

    def handle(self, *args, **kwargs):
        convert_csv_to_json(FILE_CSV_ADS,
                            FILE_JSON_ADS)

        convert_csv_to_json(FILE_CSV_CATEGORIES,
                            FILE_JSON_CATEGORIES)
