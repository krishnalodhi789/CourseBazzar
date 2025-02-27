# Generated by Django 4.2.8 on 2024-01-24 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0018_rename_course_category_coursecategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecategory',
            name='key_points',
        ),
        migrations.AlterField(
            model_name='amounttransitionhistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 17, 38, 59, 250318)),
        ),
        migrations.AlterField(
            model_name='buyhistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 17, 38, 59, 250318)),
        ),
        migrations.AlterField(
            model_name='course',
            name='published_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 17, 38, 59, 250318)),
        ),
        migrations.AlterField(
            model_name='salehistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 17, 38, 59, 250318)),
        ),
    ]
