# Generated by Django 3.0.6 on 2020-07-20 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_teacher_phone_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birthdate',
            field=models.DateField(default=datetime.date(2020, 7, 20)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone_num',
            field=models.CharField(max_length=40, null=True),
        ),
    ]