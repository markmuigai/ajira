# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 21:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ajira_parameters', '0002_auto_20170519_2128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='country_short_name',
            new_name='country_abbr',
        ),
    ]