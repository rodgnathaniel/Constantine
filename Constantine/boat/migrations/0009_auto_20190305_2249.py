# Generated by Django 2.1.5 on 2019-03-05 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0008_auto_20190305_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mode',
            name='game',
        ),
        migrations.RemoveField(
            model_name='mode',
            name='game_mode',
        ),
        migrations.AddField(
            model_name='mode',
            name='name',
            field=models.CharField(default=200, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mode',
            name='snowman_delay',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
    ]
