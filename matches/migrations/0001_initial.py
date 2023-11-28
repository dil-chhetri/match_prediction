# Generated by Django 4.2.7 on 2023-11-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=255)),
                ('time', models.CharField(max_length=255)),
                ('comp', models.CharField(max_length=255)),
                ('round', models.CharField(max_length=255)),
                ('day', models.CharField(max_length=255)),
                ('venue', models.CharField(max_length=255)),
                ('result', models.CharField(max_length=255)),
                ('gf', models.IntegerField()),
                ('ga', models.IntegerField()),
                ('opponent', models.CharField(max_length=255)),
                ('xg', models.DecimalField(decimal_places=1, max_digits=2)),
                ('xga', models.DecimalField(decimal_places=1, max_digits=2)),
                ('poss', models.IntegerField()),
                ('attendance', models.BigIntegerField()),
                ('captain', models.CharField(max_length=255)),
                ('formation', models.CharField(max_length=255)),
                ('referee', models.CharField(max_length=255)),
                ('sh', models.IntegerField()),
                ('sot', models.IntegerField()),
                ('dist', models.DecimalField(decimal_places=1, max_digits=3)),
                ('fk', models.IntegerField()),
                ('pickem', models.IntegerField()),
                ('pkatt', models.IntegerField()),
                ('season', models.IntegerField()),
                ('team', models.CharField(max_length=255)),
            ],
        ),
    ]