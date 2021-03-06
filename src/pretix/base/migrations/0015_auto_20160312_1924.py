# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-12 19:24
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0014_invoice_additional_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='is_cancelled',
        ),
        migrations.AddField(
            model_name='invoice',
            name='is_cancellation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='invoice',
            name='refers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='refered', to='pretixbase.Invoice'),
        ),
    ]
