# Generated by Django 3.1.1 on 2020-10-20 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='links',
            fields=[
                ('movieid', models.IntegerField(primary_key=True, serialize=False)),
                ('imbdid', models.IntegerField(unique=True)),
                ('tmdbid', models.IntegerField(unique=True)),
            ],
        ),
    ]
