# Generated by Django 4.0.3 on 2022-05-04 06:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_alter_articlepost_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 4, 6, 12, 56, 300099, tzinfo=utc)),
        ),
    ]
