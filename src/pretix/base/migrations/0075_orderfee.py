# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 14:35
from __future__ import unicode_literals

from decimal import Decimal

import django.db.models.deletion
from django.db import migrations, models


def fee_converter(app, schema_editor):
    OrderFee = app.get_model('pretixbase', 'OrderFee')
    Order = app.get_model('pretixbase', 'Order')

    of = []
    for o in Order.objects.exclude(payment_fee=Decimal('0.00')).iterator():
        of.append(OrderFee(
            order=o,
            value=o.payment_fee,
            fee_type='payment',
            tax_rate=o.payment_fee_tax_rate,
            tax_rule=o.payment_fee_tax_rule,
            tax_value=o.payment_fee_tax_value
        ))
        if len(of) > 900:
            OrderFee.objects.bulk_create(of)
            of = []
    OrderFee.objects.bulk_create(of)


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0074_auto_20170825_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Value')),
                ('description', models.CharField(blank=True, max_length=190)),
                ('fee_type', models.CharField(choices=[('payment', 'Payment method fee'), ('shipping', 'Shipping fee')], max_length=100)),
                ('tax_rate', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Tax rate')),
                ('tax_value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tax value')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fees', to='pretixbase.Order', verbose_name='Order')),
                ('tax_rule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pretixbase.TaxRule')),
            ],
        ),
        migrations.RunPython(
            fee_converter, migrations.RunPython.noop
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_fee',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_fee_tax_rate',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_fee_tax_rule',
        ),
        migrations.RemoveField(
            model_name='order',
            name='payment_fee_tax_value',
        ),
    ]
