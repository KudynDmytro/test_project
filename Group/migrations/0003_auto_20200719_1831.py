# Generated by Django 3.0.6 on 2020-07-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0002_auto_20200526_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]
