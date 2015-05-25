# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IMAPEndpoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('login', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('host', models.CharField(max_length=200)),
                ('port', models.IntegerField(default=0)),
                ('encryption', models.CharField(max_length=200)),
                ('dossier_racine', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Migration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('creation_date', models.DateTimeField(verbose_name='Date créée')),
                ('processing_date', models.DateTimeField(verbose_name='Date de démarrage')),
                ('completion_date', models.DateTimeField(verbose_name='Date de fin')),
                ('source', models.OneToOneField(related_name='target_migration', to='migrator.IMAPEndpoint')),
                ('target', models.OneToOneField(related_name='source_migration', to='migrator.IMAPEndpoint')),
            ],
        ),
    ]
