# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrator', '0011_auto_20150701_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imapendpoint',
            name='path',
            field=models.CharField(verbose_name='path', max_length=200),
        ),
    ]
