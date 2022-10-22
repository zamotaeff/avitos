from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='Категория')

    class Meta:
        ordering = ()
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ad(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name='Название')
    author = models.ForeignKey(User,
                               verbose_name='Пользователь',
                               on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=1000, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField('uploads/images/')
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 on_delete=models.CASCADE)

    class Meta:
        ordering = ()
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
