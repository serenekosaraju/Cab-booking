# Generated by Django 2.0.7 on 2018-07-15 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayacab', '0005_auto_20180715_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='status',
            field=models.CharField(choices=[('ONLINE', 'ONLINE'), ('OFFLINE', 'OFFLINE'), ('BOOKED', 'BOOKED')], default='OFFLINE', max_length=10),
        ),
    ]