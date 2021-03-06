# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Athist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.CharField(max_length=25)),
                ('status', models.CharField(max_length=25)),
                ('source', models.CharField(max_length=25)),
                ('destination', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Bulkhist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=25)),
                ('amount', models.CharField(max_length=25)),
                ('status', models.CharField(max_length=25)),
                ('destination', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Buyhist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('amount', models.CharField(max_length=25)),
                ('status', models.CharField(max_length=25)),
                ('destination', models.CharField(max_length=25)),
            ],
        ),
    ]
