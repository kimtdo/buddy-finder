# Generated by Django 3.1.5 on 2021-04-07 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0007_remove_report_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='username',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]