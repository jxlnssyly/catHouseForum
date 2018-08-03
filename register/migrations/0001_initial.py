# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=11)),
                ('verifyCode', models.CharField(max_length=20)),
                ('loginTime', models.DateField()),
                ('registTime', models.DateField()),
            ],
        ),
    ]
