# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-09 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20151209_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='available',
            field=models.CharField(choices=[('in stock', '\u0412 \u043d\u0430\u043b\u0438\u0447\u0438\u0438'), ('custom', '\u041f\u043e \u043f\u0440\u0435\u0434\u0437\u0430\u043a\u0430\u0437\u0443')], default='in stock', max_length=8),
        ),
    ]
