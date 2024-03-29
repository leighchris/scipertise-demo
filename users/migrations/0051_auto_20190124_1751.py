# Generated by Django 2.1.3 on 2019-01-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0050_customuser_software_hardware_intermediate'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_approved',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_under_review',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
