# Generated by Django 3.2.7 on 2021-09-30 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banker',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]