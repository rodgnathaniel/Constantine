# Generated by Django 2.1.5 on 2019-03-11 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0018_state_scroll_is'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='lucario_collision',
            field=models.BooleanField(),
        ),
    ]
