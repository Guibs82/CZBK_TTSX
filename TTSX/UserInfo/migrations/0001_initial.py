# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('daName', models.CharField(max_length=20, db_column=b'name')),
                ('daPhone', models.CharField(max_length=11, db_column=b'phone')),
                ('daAddress', models.CharField(max_length=50, db_column=b'address')),
                ('daPostCode', models.CharField(max_length=6, db_column=b'postcode')),
            ],
            options={
                'db_table': 'DeliveryAddress',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uName', models.CharField(unique=True, max_length=20, db_column=b'uname')),
                ('uPwd', models.CharField(max_length=20, db_column=b'upwd')),
                ('uEmail', models.CharField(max_length=30, db_column=b'uemail')),
                ('isDeleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'UserInfo',
            },
        ),
    ]
