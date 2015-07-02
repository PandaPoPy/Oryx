# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('migrator', '0007_auto_20150624_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='migration',
            name='completion_date',
            field=models.DateTimeField(verbose_name='End Date', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='migration',
            name='creation_date',
            field=models.DateTimeField(verbose_name='Created Date', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='migration',
            name='processing_date',
            field=models.DateTimeField(verbose_name='Start Date', default=django.utils.timezone.now),
        ),
    ]
