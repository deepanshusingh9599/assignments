# Generated by Django 4.2.4 on 2023-08-06 13:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='year',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(4)]),
        ),
    ]
