# Generated by Django 4.1.7 on 2023-03-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0002_rename_phone_user_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_no',
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
