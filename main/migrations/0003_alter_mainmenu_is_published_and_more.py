# Generated by Django 4.1.1 on 2023-05-24 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_mainmenu_is_published_mainmenu_name_kz_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmenu',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликованный'),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликованный'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Опубликованный'),
        ),
    ]