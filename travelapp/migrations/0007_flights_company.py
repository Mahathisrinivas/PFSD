# Generated by Django 2.2.11 on 2020-03-23 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0006_auto_20200323_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='company',
            field=models.CharField(default=' ', max_length=15),
        ),
    ]