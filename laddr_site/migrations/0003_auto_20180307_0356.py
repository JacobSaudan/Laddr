# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-07 03:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laddr_site', '0002_auto_20180307_0330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playergame',
            old_name='player',
            new_name='user_profile',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='player',
            new_name='user',
        ),
    ]