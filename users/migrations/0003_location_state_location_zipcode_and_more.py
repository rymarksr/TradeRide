# Generated by Django 4.2.7 on 2023-11-15 09:08

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='state',
            field=localflavor.us.models.USStateField(default='NY', max_length=2),
        ),
        migrations.AddField(
            model_name='location',
            name='zipcode',
            field=localflavor.us.models.USZipCodeField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='location',
            name='address_1',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
