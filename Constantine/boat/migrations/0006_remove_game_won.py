# Generated by Django 2.1.5 on 2019-03-01 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0005_auto_20190301_0504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='won',
        ),
    ]
