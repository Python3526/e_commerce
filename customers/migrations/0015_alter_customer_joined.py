# Generated by Django 5.0.7 on 2024-07-21 05:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0014_alter_customer_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 21, 10, 16, 23, 948034)),
        ),
    ]