# Generated by Django 4.1.1 on 2023-05-25 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_mainmenu_test_editor_alter_mainmenu_name_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainmenu',
            name='test_editor',
        ),
    ]
