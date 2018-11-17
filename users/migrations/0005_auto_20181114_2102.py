# Generated by Django 2.0.5 on 2018-11-14 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='skills',
            field=models.ManyToManyField(blank=True, to='users.Skill'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
