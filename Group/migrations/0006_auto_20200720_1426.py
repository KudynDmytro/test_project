# Generated by Django 3.0.6 on 2020-07-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0005_auto_20200720_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_id',
            field=models.IntegerField(null=True),
        ),
    ]