# Generated by Django 3.0.6 on 2020-07-19 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_auto_20200526_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birthdate',
            field=models.DateField(default=datetime.date(2020, 7, 19)),
        ),
    ]
