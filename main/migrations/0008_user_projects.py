# Generated by Django 2.0 on 2020-04-07 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200407_1145'),
        ('main', '0007_auto_20200228_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='projects',
            field=models.ManyToManyField(blank=True, to='projects.Projects'),
        ),
    ]
