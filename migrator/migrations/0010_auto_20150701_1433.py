# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrator', '0009_auto_20150701_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='migration',
            name='creation_date',
            field=models.DateTimeField(verbose_name='Created Date', auto_now_add=True),
        ),
    ]
