# Generated by Django 2.0.7 on 2018-07-17 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayacab', '0010_auto_20180717_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='commuter',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='commuter',
            name='long',
            field=models.FloatField(blank=True, null=True),
        ),
    ]