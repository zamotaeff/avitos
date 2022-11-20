from datetime import date

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from users.validators import check_birth_date


class Location(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Название')
    lat = models.DecimalField(max_digits=8,
                              decimal_places=6,
                              verbose_name='Широта',
                              null=True)
    lng = models.DecimalField(max_digits=8,
                              decimal_places=6,
                              verbose_name='Долгота',
                              null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ()
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class UserRoles:
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    choices = [
        (MEMBER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    ]


class User(AbstractUser):
    first_name = models.CharField(max_length=30,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=50,
                                 verbose_name='Фамилия')
    username = models.CharField(max_length=50,
                                verbose_name='Никнейм',
                                unique=True)
    password = models.CharField(max_length=50,
                                verbose_name='Пароль')
    role = models.CharField(max_length=10,
                            verbose_name='Роль пользователя',
                            choices=UserRoles.choices,
                            default=UserRoles.MEMBER)
    birth_date = models.DateTimeField(validators=[check_birth_date],
                                      verbose_name='Дата рождения',
                                      null=True,
                                      blank=True)
    email = models.EmailField(verbose_name='email address',
                              blank=True,
                              validators=[RegexValidator(
                                  regex="@rambler.ru",
                                  inverse_match=True,
                                  message="Домен rambler запрещен.")])
    age = models.PositiveSmallIntegerField(verbose_name='Возраст',
                                           editable=False)
    location = models.ManyToManyField(Location,
                                      verbose_name='Локация')

    def save(self, *args, **kwargs):
        self.age = relativedelta(date.today(), self.birth_date).year
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
