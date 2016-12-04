# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 22:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', tinymce.models.HTMLField()),
                ('url', models.URLField()),
                ('is_published', models.BooleanField(default=False)),
                ('published_on', models.DateTimeField(default=datetime.datetime.now)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
