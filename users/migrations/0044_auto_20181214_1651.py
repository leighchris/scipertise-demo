# Generated by Django 2.0.5 on 2018-12-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_auto_20181212_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='skill_area1_title',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='skill_area2_title',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='skill_area3_title',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='skill_area4_title',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='skill_area5_title',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
    ]