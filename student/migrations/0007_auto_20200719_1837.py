# Generated by Django 3.0.6 on 2020-07-19 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_student_phone_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_num',
            field=models.CharField(max_length=40, null=True),
        ),
    ]