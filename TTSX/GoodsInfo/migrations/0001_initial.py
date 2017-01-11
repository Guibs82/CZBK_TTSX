# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gTitle', models.CharField(max_length=20, db_column=b'gtitle')),
                ('gImage', models.CharField(max_length=100, db_column=b'gimage')),
                ('gPrice', models.DecimalField(decimal_places=2, max_digits=10, db_column=b'gprice')),
                ('gDesc', models.TextField(max_length=500, db_column=b'gdesc')),
                ('isDeleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'GoodsInfo',
            },
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tTitle', models.CharField(max_length=20, db_column=b'ttitle')),
                ('isDeleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'TypeInfo',
            },
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gType',
            field=models.ForeignKey(to='GoodsInfo.TypeInfo', db_column=b'gtype'),
        ),
    ]
