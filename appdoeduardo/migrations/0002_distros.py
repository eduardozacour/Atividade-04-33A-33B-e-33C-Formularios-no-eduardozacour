# Generated by Django 3.2.13 on 2023-09-06 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdoeduardo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distros',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('available', models.CharField(max_length=50)),
            ],
        ),
    ]