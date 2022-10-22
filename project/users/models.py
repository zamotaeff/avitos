from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Название')
    lat = models.DecimalField(max_digits=8,
                              decimal_places=6,
                              verbose_name='Широта')
    lng = models.DecimalField(max_digits=8,
                              decimal_places=6,
                              verbose_name='Долгота')

    class Meta:
        ordering = ()
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class User(models.Model):
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    USER_ROLE_CHOICES = [
        (MEMBER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Администратор'),
    ]

    first_name = models.CharField(max_length=30,
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=50,
                                 verbose_name='Фамилия')
    username = models.CharField(max_length=50,
                                verbose_name='Никнейм',
                                unique=True)
    password = models.CharField(max_length=50,
                                verbose_name='Пароль')
    role = models.CharField(max_length=9,
                            verbose_name='Роль пользователя',
                            choices=USER_ROLE_CHOICES,
                            default=MEMBER)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст')
    location = models.ForeignKey(Location,
                                 verbose_name='Локация',
                                 on_delete=models.CASCADE)

    class Meta:
        ordering = ()
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
