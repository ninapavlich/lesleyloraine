# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailcategory',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='emailcategorysubscriptionsettings',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='emailreceipt',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='emailtemplate',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
        migrations.AlterField(
            model_name='usersubscriptionsettings',
            name='admin_note',
            field=models.TextField(help_text=b'Not publicly visible', null=True, verbose_name='admin note', blank=True),
        ),
    ]
