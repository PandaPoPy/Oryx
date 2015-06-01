# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrator', '0003_auto_20150527_1017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imapendpoint',
            old_name='login',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='imapendpoint',
            name='encryption',
            field=models.CharField(default='NO', choices=[('NO', 'None'), ('SSL', 'SSL/TLS'), ('START', 'STARTTLS')], verbose_name='Encryption choice', max_length=8),
        ),
        migrations.AlterField(
            model_name='imapendpoint',
            name='host',
            field=models.CharField(verbose_name='Your Host :', max_length=100),
        ),
        migrations.AlterField(
            model_name='imapendpoint',
            name='origin_file',
            field=models.CharField(verbose_name='Origin File', max_length=200),
        ),
        migrations.AlterField(
            model_name='imapendpoint',
            name='password',
            field=models.CharField(verbose_name='Password :', max_length=200),
        ),
        migrations.AlterField(
            model_name='imapendpoint',
            name='port',
            field=models.IntegerField(default=143, verbose_name='Your Port :'),
        ),
    ]
