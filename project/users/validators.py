from dateutil.relativedelta import relativedelta
from datetime import date
from django.core.exceptions import ValidationError


def check_birth_date(birth_date):
    diff = relativedelta(date.today(), birth_date).years
    if diff < 9:
        raise ValidationError("Регистрация пользователя с 9 лет.")
