# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-22 09:07
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainusers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'ordering': ['-retail_order', 'product'],
            },
        ),
        migrations.CreateModel(
            name='Retail_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('order_date', models.DateField(default=datetime.datetime(2017, 2, 22, 9, 7, 43, 194337, tzinfo=utc))),
                ('status', models.CharField(choices=[('DFT', 'Draf'), ('CNF', 'Confirmed'), ('INP', 'In Progress'), ('DIS', 'Dispatched'), ('DLV', 'Delivered')], max_length=4)),
                ('retail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainusers.Retail')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-order_date'],
            },
        ),
        migrations.AddField(
            model_name='order_details',
            name='retail_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Retail_order'),
        ),
    ]
