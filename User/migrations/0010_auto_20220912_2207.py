# Generated by Django 3.2.7 on 2022-09-12 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_auto_20211108_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='any_disease',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_donate_date',
        ),
    ]
