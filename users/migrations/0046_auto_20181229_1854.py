# Generated by Django 2.1.3 on 2018-12-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0045_customuser_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='expert',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gives_tutorials',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]