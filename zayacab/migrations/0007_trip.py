# Generated by Django 2.0.7 on 2018-07-15 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zayacab', '0006_auto_20180715_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('fare', models.IntegerField()),
            ],
        ),
    ]
