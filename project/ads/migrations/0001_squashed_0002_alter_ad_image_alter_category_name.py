# Generated by Django 4.0.1 on 2022-10-24 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [('ads', '0001_initial'), ('ads', '0002_alter_ad_image_alter_category_name')]

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': (),
            },
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=1000, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user',
                                             verbose_name='Пользователь')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.category',
                                               verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
                'ordering': (),
            },
        ),
    ]
