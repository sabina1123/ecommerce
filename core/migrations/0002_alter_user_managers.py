# Generated by Django 5.1.5 on 2025-01-26 13:34

import core.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', core.managers.UserManager()),
            ],
        ),
    ]
