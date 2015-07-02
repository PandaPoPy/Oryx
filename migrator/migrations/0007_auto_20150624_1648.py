# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrator', '0006_auto_20150601_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imapendpoint',
            name='encryption_imap',
            field=models.CharField(choices=[('SSL', 'SSL/TLS'), ('START', 'STARTTLS')], max_length=8, default='START', verbose_name='encryption'),
        ),
    ]
