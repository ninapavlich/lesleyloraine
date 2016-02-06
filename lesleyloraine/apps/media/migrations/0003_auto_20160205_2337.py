# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20160130_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_width',
        ),
        migrations.RemoveField(
            model_name='media',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='media',
            name='image_width',
        ),
        migrations.AlterField(
            model_name='image',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='mediatag',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
    ]
