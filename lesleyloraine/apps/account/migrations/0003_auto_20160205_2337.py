# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160130_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='organizationmember',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='socialcontactlink',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='usergroupmember',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
    ]
