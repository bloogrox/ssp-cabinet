# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 23:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CampaignFilter',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('value', models.CharField(max_length=1024)),
                ('campaign', models.ForeignKey(on_delete=(django.db.models
                                                          .deletion.CASCADE),
                                               to='campaigns.Campaign')),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='campaignfilter',
            name='field',
            field=models.ForeignKey(on_delete=(django.db.models
                                               .deletion.CASCADE),
                                    to='campaigns.Field'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='targetings',
            field=models.ManyToManyField(through='campaigns.CampaignFilter',
                                         to='campaigns.Field'),
        ),
        migrations.AlterUniqueTogether(
            name='campaignfilter',
            unique_together=set([('campaign', 'field')]),
        ),
    ]
