# Generated by Django 2.0.3 on 2018-04-01 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('C', 'Comedy'), ('D', 'Documentary'), ('H', 'Horror'), ('RC', 'Romantic Comedy'), ('SF', 'Sci-Fi'), ('D', 'Drama'), ('Cl', 'Classic'), ('CC', 'Cult Classic')], default='D', max_length=2),
        ),
        migrations.AddField(
            model_name='movie',
            name='comments',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='movie',
            name='seen_on',
            field=models.DateField(default=datetime.date.today),
        ),
    ]