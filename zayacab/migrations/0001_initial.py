# Generated by Django 2.0.7 on 2018-07-13 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('opening', models.FloatField()),
                ('closing', models.FloatField()),
                ('volume', models.IntegerField()),
            ],
        ),
    ]
