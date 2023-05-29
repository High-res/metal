# Generated by Django 4.1.1 on 2023-05-25 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_mainmenu_test_editor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Название картинки')),
                ('picture', models.ImageField(null=True, upload_to='static/', verbose_name='Logo компании')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликованный')),
            ],
            options={
                'verbose_name': 'картинка',
                'verbose_name_plural': 'Галерея',
            },
        ),
    ]
