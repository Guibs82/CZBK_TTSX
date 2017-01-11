# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserInfo', '0002_deliveryaddress_daowner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uPwd',
            field=models.CharField(max_length=40, db_column=b'upwd'),
        ),
    ]
