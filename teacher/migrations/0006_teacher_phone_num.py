# Generated by Django 3.0.6 on 2020-07-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_auto_20200719_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='phone_num',
            field=models.CharField(default=380123456789, max_length=20),
            preserve_default=False,
        ),
    ]
