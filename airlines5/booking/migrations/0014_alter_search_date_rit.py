# Generated by Django 4.0.3 on 2022-04-23 18:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_alter_aes_s1_alter_aes_s2_alter_search_date_rit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='date_rit',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 4, 23, 18, 27, 54, 417629), null=True),
        ),
    ]
