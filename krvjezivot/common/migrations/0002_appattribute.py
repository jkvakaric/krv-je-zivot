# Generated by Django 2.0.5 on 2018-05-23 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppAttribute',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=255, verbose_name='attribute key')),
                ('py_type', models.CharField(max_length=255, verbose_name='python type')),
                ('value', models.CharField(max_length=255, verbose_name='value as string')),
            ],
        ),
    ]