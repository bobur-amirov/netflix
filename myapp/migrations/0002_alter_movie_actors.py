# Generated by Django 3.2.6 on 2021-08-17 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='actors', to='myapp.Actor'),
        ),
    ]
