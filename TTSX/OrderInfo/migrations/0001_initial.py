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
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oiCount', models.IntegerField(db_column=b'count')),
                ('oiPrice', models.DecimalField(decimal_places=2, max_digits=10, db_column=b'price')),
                ('oiGoods', models.ForeignKey(to='GoodsInfo.GoodsInfo', db_column=b'goods')),
            ],
            options={
                'db_table': 'OrderDetailInfo',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oTotal', models.DecimalField(decimal_places=2, max_digits=10, db_column=b'ototal')),
                ('oTime', models.DateTimeField(auto_now_add=True, db_column=b'otime')),
                ('oState', models.BooleanField(default=False, db_column=b'state')),
                ('oUser', models.ForeignKey(to='UserInfo.UserInfo', db_column=b'user')),
            ],
            options={
                'db_table': 'OrderInfo',
            },
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='oiOrder',
            field=models.ForeignKey(to='OrderInfo.OrderInfo', db_column=b'order'),
        ),
    ]
