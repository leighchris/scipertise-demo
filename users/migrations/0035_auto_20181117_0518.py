# Generated by Django 2.0.5 on 2018-11-17 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_customuser_skills'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='skills',
            new_name='tags',
        ),
    ]
