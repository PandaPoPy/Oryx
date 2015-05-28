# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('migrator', '0002_auto_20150519_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imapendpoint',
            old_name='dossier_racine',
            new_name='origin_file',
        ),
        migrations.RenameField(
            model_name='migration',
            old_name='source',
            new_name='origin',
        ),
        migrations.AlterField(
            model_name='imapendpoint',
            name='port',
            field=models.IntegerField(default=143),
        ),
        migrations.AlterField(
            model_name='migration',
            name='completion_date',
            field=models.DateTimeField(verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='migration',
            name='creation_date',
            field=models.DateTimeField(verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='migration',
            name='processing_date',
            field=models.DateTimeField(verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='migration',
            name='target',
            field=models.OneToOneField(to='migrator.IMAPEndpoint', related_name='origin_migration'),
        ),
    ]
