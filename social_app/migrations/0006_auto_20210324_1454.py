# Generated by Django 3.1.5 on 2021-03-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0005_auto_20210324_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
    ]
