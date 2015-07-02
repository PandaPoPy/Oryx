# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrator', '0005_auto_20150529_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imapendpoint',
            old_name='email',
            new_name='email_imap',
        ),
        migrations.RenameField(
            model_name='imapendpoint',
            old_name='encryption',
            new_name='encryption_imap',
        ),
        migrations.RenameField(
            model_name='imapendpoint',
            old_name='host',
            new_name='host_imap',
        ),
        migrations.RenameField(
            model_name='imapendpoint',
            old_name='origin_file',
            new_name='origin_file_imap',
        ),
        migrations.RenameField(
            model_name='imapendpoint',
            old_name='password',
            new_name='password_imap',
        ),
        migrations.RenameField(
            model_name='imapendpoint',
            old_name='port',
            new_name='port_imap',
        ),
    ]
