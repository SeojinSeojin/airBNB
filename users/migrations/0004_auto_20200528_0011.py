# Generated by Django 2.2.5 on 2020-05-27 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200527_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email_verifid',
            new_name='email_verified',
        ),
    ]
