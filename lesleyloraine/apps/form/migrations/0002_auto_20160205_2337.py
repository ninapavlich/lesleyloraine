# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldentry',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='form',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='formentry',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='formentrystatus',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='formentrytag',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
    ]
