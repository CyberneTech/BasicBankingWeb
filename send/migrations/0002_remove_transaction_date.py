# Generated by Django 3.1.5 on 2021-02-16 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('send', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='date',
        ),
    ]
