# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imapendpoint',
            name='encryption',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='imapendpoint',
            name='host',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='imapendpoint',
            name='login',
            field=models.EmailField(verbose_name='email', max_length=254),
        ),
    ]
