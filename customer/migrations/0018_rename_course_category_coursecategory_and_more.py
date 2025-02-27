# Generated by Django 4.2.8 on 2024-01-24 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_course_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course_Category',
            new_name='CourseCategory',
        ),
        migrations.AlterField(
            model_name='amounttransitionhistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 17, 37, 40, 815555)),
        ),
        migrations.AlterField(
            model_name='buyhistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 17, 37, 40, 815555)),
        ),
        migrations.AlterField(
            model_name='course',
            name='published_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 17, 37, 40, 815555)),
        ),
        migrations.AlterField(
            model_name='salehistory',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 17, 37, 40, 815555)),
        ),
    ]
