# Generated by Django 4.1.7 on 2023-03-18 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone',
            new_name='phone_no',
        ),
    ]
