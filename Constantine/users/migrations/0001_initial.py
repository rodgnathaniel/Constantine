# Generated by Django 2.1.5 on 2019-02-22 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player_Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('games_lost', models.IntegerField(blank=True, null=True)),
                ('games_won', models.IntegerField(blank=True, null=True)),
                ('game_times', models.CharField(max_length=120)),
            ],
        ),
    ]
