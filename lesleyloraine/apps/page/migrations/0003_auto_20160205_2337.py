# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20160130_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalcontentblock',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='pagecontentblock',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='pageslide',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
    ]
