# Generated by Django 3.0.5 on 2020-05-04 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('bionominal', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('sun_pref', models.CharField(choices=[(1, 'High'), (2, 'Med/High'), (3, 'Med'), (4, 'Med/Low'), (5, 'Low'), (6, 'Any')], max_length=1)),
                ('water_freq', models.IntegerField()),
                ('fertilizer_freq', models.IntegerField()),
            ],
        ),
    ]
