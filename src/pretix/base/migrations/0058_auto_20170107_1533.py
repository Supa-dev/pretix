# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 15:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0057_auto_20170107_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='familyname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='givenname',
        ),
    ]