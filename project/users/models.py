from django.contrib.auth.models import AbstractUser
from django.db import models


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
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    location = models.ManyToManyField(Location,
                                      verbose_name='Локация')

    def __str__(self):
        return f'{self.username}'

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
