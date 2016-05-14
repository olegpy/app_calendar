# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('credit', models.IntegerField()),
                ('debet', models.IntegerField()),
                ('start_agreement', models.DateField()),
                ('end_agreement', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=200)),
                ('iso', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('choice', models.ForeignKey(to='agreements.Agreement')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.ForeignKey(to='agreements.Country'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='company',
            field=models.ForeignKey(to='agreements.Company'),
        ),
        migrations.AddField(
            model_name='agreement',
            name='negotiator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
