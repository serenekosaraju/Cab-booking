# Generated by Django 2.0.7 on 2018-07-15 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zayacab', '0008_auto_20180715_0925'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dummy',
        ),
        migrations.AddField(
            model_name='trip',
            name='commuter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commuter', to='zayacab.Commuter'),
        ),
        migrations.AddField(
            model_name='trip',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver', to='zayacab.Driver'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='status',
            field=models.CharField(choices=[('AV', 'AVAILABLE'), ('OFF', 'OFFLINE'), ('BK', 'BOOKED')], default='OFFLINE', max_length=10),
        ),
    ]
