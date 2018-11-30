# Generated by Django 2.0.5 on 2018-11-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20181130_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='completeDateTime',
        ),
        migrations.AddField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(null=True, verbose_name='End time'),
        ),
        migrations.AddField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(null=True, verbose_name='Start time'),
        ),
    ]
