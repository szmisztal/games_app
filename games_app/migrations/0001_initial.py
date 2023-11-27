# Generated by Django 4.2.2 on 2023-06-25 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Development_Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('genre', models.PositiveSmallIntegerField(blank=True, choices=[], default=0)),
                ('premiere', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='games_app.development_studio')),
            ],
        ),
    ]
