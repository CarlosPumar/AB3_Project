# Generated by Django 3.2.7 on 2021-10-05 22:41

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='relation',
            managers=[
                ('manager_extend', django.db.models.manager.Manager()),
            ],
        ),
    ]
