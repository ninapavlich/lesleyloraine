# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalContentBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('publication_date', models.DateTimeField(null=True, verbose_name='Publication Date', blank=True)),
                ('publication_status', models.IntegerField(default=10, help_text=b'Current publication status', choices=[(10, 'Draft'), (20, 'Needs Review'), (100, 'Published'), (40, 'Unpublished')])),
                ('publish_on_date', models.DateTimeField(help_text=b"Object state will be set to 'Published' on this date.", null=True, verbose_name='Publish on Date', blank=True)),
                ('expire_on_date', models.DateTimeField(help_text=b"Object state will be set to 'Expired' on this date.", null=True, verbose_name='Expire on Date', blank=True)),
                ('content', models.TextField(help_text=b'', null=True, verbose_name='content', blank=True)),
                ('synopsis', models.TextField(help_text=b'', null=True, verbose_name='synopsis', blank=True)),
                ('created_by', models.ForeignKey(related_name='page_globalcontentblock_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='page_globalcontentblock_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('published_by', models.ForeignKey(related_name='page_globalcontentblock_published_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Global Content Block',
                'verbose_name_plural': 'Global Content Blocks',
            },
        ),
        migrations.RemoveField(
            model_name='pagetag',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='pagetag',
            name='image',
        ),
        migrations.RemoveField(
            model_name='pagetag',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='pagetag',
            name='published_by',
        ),
        migrations.RemoveField(
            model_name='pagetag',
            name='social_share_image',
        ),
        migrations.RemoveField(
            model_name='pagetag',
            name='template',
        ),
        migrations.RemoveField(
            model_name='pageslide',
            name='link',
        ),
        migrations.AddField(
            model_name='page',
            name='form',
            field=models.ForeignKey(blank=True, to='form.Form', null=True),
        ),
        migrations.DeleteModel(
            name='PageTag',
        ),
    ]
