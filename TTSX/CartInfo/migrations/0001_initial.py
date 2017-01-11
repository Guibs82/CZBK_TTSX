# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserInfo', '0001_initial'),
        ('GoodsInfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cCount', models.IntegerField(db_column=b'count')),
                ('cGoods', models.ForeignKey(to='GoodsInfo.GoodsInfo', db_column=b'goods')),
                ('cUser', models.ForeignKey(to='UserInfo.UserInfo', db_column=b'user')),
            ],
            options={
                'db_table': 'CartInfo',
            },
        ),
    ]
