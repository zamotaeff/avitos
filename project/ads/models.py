from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='Категория',
                            unique=True)
    slug = models.CharField(unique=True,
                            null=True,
                            blank=True,
                            max_length=10,
                            validators=[MinLengthValidator(5),
                                       MaxLengthValidator(9)])

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ()
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ad(models.Model):
    name = models.CharField(max_length=150,
                            verbose_name='Название',
                            validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User,
                               related_name='ads',
                               verbose_name='Пользователь',
                               on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/',
                              verbose_name='Изображение',
                              null=True,
                              blank=True)
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ()
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Selection(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name
