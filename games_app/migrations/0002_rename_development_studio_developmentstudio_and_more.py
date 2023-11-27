# Generated by Django 4.2.2 on 2023-06-25 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Development_Studio',
            new_name='DevelopmentStudio',
        ),
        migrations.AlterField(
            model_name='game',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Another'), (1, 'Shooter'), (2, 'Strategy'), (3, 'RPG'), (4, 'Horror'), (5, 'Racing'), (6, 'Action'), (7, 'Adventure'), (8, 'Sports')], default=0),
        ),
    ]
