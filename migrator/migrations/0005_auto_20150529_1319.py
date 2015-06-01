# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrator', '0004_auto_20150529_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imapendpoint',
            name='encryption',
            field=models.CharField(verbose_name='encryption', default='NO', max_length=8, choices=[('NO', 'None'), ('SSL', 'SSL/TLS'), ('START', 'STARTTLS')]),
        ),
        migrations.AlterField(
            model_name='imapendpoint',
            name='host',
            field=models.CharField(verbose_name='host', max_length=100),
        ),
        migrations.AlterField(
            model_name='imapendpoint',
            name='origin_file',
            field=models.CharField(verbose_name='originfile', max_length=200),
        ),
        migrations.AlterField(
            model_name='imapendpoint',
            name='password',
            field=models.CharField(verbose_name='password', max_length=200),
        ),
        migrations.AlterField(
            model_name='imapendpoint',
            name='port',
            field=models.IntegerField(default=143, verbose_name='port'),
        ),
    ]
