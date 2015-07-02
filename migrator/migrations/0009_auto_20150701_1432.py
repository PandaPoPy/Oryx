# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrator', '0008_auto_20150630_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='migration',
            name='completion_date',
            field=models.DateTimeField(verbose_name='End Date', null=True),
        ),
        migrations.AlterField(
            model_name='migration',
            name='processing_date',
            field=models.DateTimeField(verbose_name='Start Date', null=True),
        ),
    ]
