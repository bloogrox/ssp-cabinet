# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-14 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0003_auto_20170912_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='dsp',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to='campaigns.Dsp'),
            preserve_default=False,
        ),
    ]
