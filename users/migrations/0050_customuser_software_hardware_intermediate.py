# Generated by Django 2.1.3 on 2019-01-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0049_auto_20190122_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='software_hardware_intermediate',
            field=models.CharField(blank=True, default='', max_length=10000, null=True),
        ),
    ]