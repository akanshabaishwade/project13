# Generated by Django 4.0 on 2021-12-30 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weddinginvitation',
            name='giftimage',
        ),
    ]