# Generated by Django 4.1.1 on 2023-05-29 03:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_products_main_menu_alter_submenu_main_menu'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategorymenu',
            options={'verbose_name': 'меню подкатегорий', 'verbose_name_plural': 'Меню подкатегорий'},
        ),
        migrations.RemoveField(
            model_name='subcategorymenu',
            name='promotion',
        ),
        migrations.RemoveField(
            model_name='subcategorymenu',
            name='promotion_text',
        ),
        migrations.RemoveField(
            model_name='subcategorymenu',
            name='promotion_text_kaz',
        ),
        migrations.RemoveField(
            model_name='submenu',
            name='promotion',
        ),
        migrations.RemoveField(
            model_name='submenu',
            name='promotion_text',
        ),
        migrations.RemoveField(
            model_name='submenu',
            name='promotion_text_kaz',
        ),
        migrations.AlterField(
            model_name='products',
            name='main_menu',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.subcategorymenu'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submenu',
            name='main_menu',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.mainmenu'),
            preserve_default=False,
        ),
    ]