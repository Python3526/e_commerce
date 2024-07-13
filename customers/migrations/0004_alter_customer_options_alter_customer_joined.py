# Generated by Django 5.0.7 on 2024-07-13 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_customer_joined'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['id'], 'verbose_name_plural': 'All Customers'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 13, 16, 56, 21, 668155)),
        ),
    ]