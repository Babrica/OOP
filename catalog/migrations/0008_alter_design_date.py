# Generated by Django 4.2.5 on 2023-09-11 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20221122_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 11, 19, 51, 13, 312884), null=True, verbose_name='Дата'),
        ),
    ]
