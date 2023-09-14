# Generated by Django 3.2.16 on 2022-11-22 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_design_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='Эскиз', help_text='Категории', max_length=30, unique=True, verbose_name='Категории'),
        ),
        migrations.AlterField(
            model_name='design',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 22, 16, 18, 34, 66880), null=True, verbose_name='Дата'),
        ),
    ]
