# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrator', '0010_auto_20150701_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imapendpoint',
            old_name='origin_file_imap',
            new_name='path',
        ),
    ]
