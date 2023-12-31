# Generated by Django 4.2.5 on 2023-09-24 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_user_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='access',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
