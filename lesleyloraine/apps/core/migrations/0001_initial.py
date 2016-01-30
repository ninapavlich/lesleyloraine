# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import carbon.compounds.core.models
import lesleyloraine.s3utils
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAppGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('uuid', models.CharField(help_text=b'UUID generated for object; can be used for short URLs', max_length=255, verbose_name='UUID', blank=True)),
                ('order', models.IntegerField(default=0, help_text=b'')),
                ('path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='path', blank=True)),
                ('title_path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True)),
                ('path_generated', models.CharField(help_text=b'The URL path to this page, based on page hierarchy and slug.', max_length=255, null=True, verbose_name='generated path', blank=True)),
                ('path_override', models.CharField(help_text=b'The URL path to this page, defined absolutely.', max_length=255, null=True, verbose_name='path override', blank=True)),
                ('hierarchy', models.CharField(null=True, max_length=255, blank=True, help_text=b'Administrative Hierarchy', unique=True, verbose_name='hierarchy')),
                ('temporary_redirect', models.CharField(help_text=b'Temporarily redirect to a different path', max_length=255, verbose_name='Temporary Redirect', blank=True)),
                ('permanent_redirect', models.CharField(help_text=b'Permanently redirect to a different path', max_length=255, verbose_name='Permanent Redirect', blank=True)),
                ('created_by', models.ForeignKey(related_name='core_adminappgroup_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='core_adminappgroup_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdminAppLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('uuid', models.CharField(help_text=b'UUID generated for object; can be used for short URLs', max_length=255, verbose_name='UUID', blank=True)),
                ('order', models.IntegerField(default=0, help_text=b'')),
                ('path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='path', blank=True)),
                ('title_path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True)),
                ('path_generated', models.CharField(help_text=b'The URL path to this page, based on page hierarchy and slug.', max_length=255, null=True, verbose_name='generated path', blank=True)),
                ('path_override', models.CharField(help_text=b'The URL path to this page, defined absolutely.', max_length=255, null=True, verbose_name='path override', blank=True)),
                ('hierarchy', models.CharField(null=True, max_length=255, blank=True, help_text=b'Administrative Hierarchy', unique=True, verbose_name='hierarchy')),
                ('temporary_redirect', models.CharField(help_text=b'Temporarily redirect to a different path', max_length=255, verbose_name='Temporary Redirect', blank=True)),
                ('permanent_redirect', models.CharField(help_text=b'Permanently redirect to a different path', max_length=255, verbose_name='Permanent Redirect', blank=True)),
                ('model_path', models.CharField(help_text=b'e.x. blog.models.BlogArticle', max_length=255, verbose_name='Model Path', db_index=True)),
                ('created_by', models.ForeignKey(related_name='core_adminapplink_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='core_adminapplink_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', models.ForeignKey(blank=True, to='core.AdminAppGroup', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdminLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('uuid', models.CharField(help_text=b'UUID generated for object; can be used for short URLs', max_length=255, verbose_name='UUID', blank=True)),
                ('order', models.IntegerField(default=0, help_text=b'')),
                ('path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='path', blank=True)),
                ('title_path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True)),
                ('path_generated', models.CharField(help_text=b'The URL path to this page, based on page hierarchy and slug.', max_length=255, null=True, verbose_name='generated path', blank=True)),
                ('path_override', models.CharField(help_text=b'The URL path to this page, defined absolutely.', max_length=255, null=True, verbose_name='path override', blank=True)),
                ('hierarchy', models.CharField(null=True, max_length=255, blank=True, help_text=b'Administrative Hierarchy', unique=True, verbose_name='hierarchy')),
                ('temporary_redirect', models.CharField(help_text=b'Temporarily redirect to a different path', max_length=255, verbose_name='Temporary Redirect', blank=True)),
                ('permanent_redirect', models.CharField(help_text=b'Permanently redirect to a different path', max_length=255, verbose_name='Permanent Redirect', blank=True)),
                ('url', models.CharField(help_text=b'', max_length=255, verbose_name='URL', db_index=True)),
                ('created_by', models.ForeignKey(related_name='core_adminlink_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='core_adminlink_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AdminSidebar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('uuid', models.CharField(help_text=b'UUID generated for object; can be used for short URLs', max_length=255, verbose_name='UUID', blank=True)),
                ('order', models.IntegerField(default=0, help_text=b'')),
                ('path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='path', blank=True)),
                ('title_path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True)),
                ('path_generated', models.CharField(help_text=b'The URL path to this page, based on page hierarchy and slug.', max_length=255, null=True, verbose_name='generated path', blank=True)),
                ('path_override', models.CharField(help_text=b'The URL path to this page, defined absolutely.', max_length=255, null=True, verbose_name='path override', blank=True)),
                ('hierarchy', models.CharField(null=True, max_length=255, blank=True, help_text=b'Administrative Hierarchy', unique=True, verbose_name='hierarchy')),
                ('temporary_redirect', models.CharField(help_text=b'Temporarily redirect to a different path', max_length=255, verbose_name='Temporary Redirect', blank=True)),
                ('permanent_redirect', models.CharField(help_text=b'Permanently redirect to a different path', max_length=255, verbose_name='Permanent Redirect', blank=True)),
                ('created_by', models.ForeignKey(related_name='core_adminsidebar_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='core_adminsidebar_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CSSPackage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('peg_revision', models.PositiveIntegerField(help_text=b'While making unstable changes, you may peg the package         to last working version number. Then newer packages will only be         returned if settings.DEBUG=True. Leave blank to use the lastest version.', null=True, blank=True)),
                ('generated_file_source', models.TextField(null=True, blank=True)),
                ('generated_file_minified', models.TextField(null=True, blank=True)),
                ('error_source_content', models.TextField(null=True, blank=True)),
                ('file_source', models.FileField(storage=lesleyloraine.s3utils._MediaS3BotoStorage(bucket=b'lesleyloraine', custom_domain=b'lesleyloraine.s3.amazonaws.com', location=b'media'), null=True, upload_to=carbon.compounds.core.models.title_file_name, blank=True)),
                ('file_minified', models.FileField(storage=lesleyloraine.s3utils._MediaS3BotoStorage(bucket=b'lesleyloraine', custom_domain=b'lesleyloraine.s3.amazonaws.com', location=b'media'), null=True, upload_to=carbon.compounds.core.models.title_file_name, blank=True)),
                ('needs_render', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(related_name='core_csspackage_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='core_csspackage_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CSSResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('order', models.IntegerField(default=0, help_text=b'')),
                ('custom_source', models.TextField(help_text=b'Set the source of this resource', null=True, verbose_name='custom source', blank=True)),
                ('file_source_url', models.CharField(help_text=b'URL to an existing resource', max_length=255, null=True, verbose_name='File Source', blank=True)),
                ('file_source_path', models.CharField(help_text=b'Relative source path, if file_source_url is a package', max_length=255, null=True, verbose_name='File Source Path', blank=True)),
                ('compiler', models.CharField(default=b'css', max_length=255, verbose_name=b'Compiler / Preprocessor', choices=[(b'css', b'CSS (None)'), (b'scss', b'SCSS')])),
                ('created_by', models.ForeignKey(related_name='core_cssresource_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='core_cssresource_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', models.ForeignKey(to='core.CSSPackage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JSPackage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('peg_revision', models.PositiveIntegerField(help_text=b'While making unstable changes, you may peg the package         to last working version number. Then newer packages will only be         returned if settings.DEBUG=True. Leave blank to use the lastest version.', null=True, blank=True)),
                ('generated_file_source', models.TextField(null=True, blank=True)),
                ('generated_file_minified', models.TextField(null=True, blank=True)),
                ('error_source_content', models.TextField(null=True, blank=True)),
                ('file_source', models.FileField(storage=lesleyloraine.s3utils._MediaS3BotoStorage(bucket=b'lesleyloraine', custom_domain=b'lesleyloraine.s3.amazonaws.com', location=b'media'), null=True, upload_to=carbon.compounds.core.models.title_file_name, blank=True)),
                ('file_minified', models.FileField(storage=lesleyloraine.s3utils._MediaS3BotoStorage(bucket=b'lesleyloraine', custom_domain=b'lesleyloraine.s3.amazonaws.com', location=b'media'), null=True, upload_to=carbon.compounds.core.models.title_file_name, blank=True)),
                ('needs_render', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(related_name='core_jspackage_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='core_jspackage_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JSResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('order', models.IntegerField(default=0, help_text=b'')),
                ('custom_source', models.TextField(help_text=b'Set the source of this resource', null=True, verbose_name='custom source', blank=True)),
                ('file_source_url', models.CharField(help_text=b'URL to an existing resource', max_length=255, null=True, verbose_name='File Source', blank=True)),
                ('file_source_path', models.CharField(help_text=b'Relative source path, if file_source_url is a package', max_length=255, null=True, verbose_name='File Source Path', blank=True)),
                ('compiler', models.CharField(default=b'js', max_length=255, verbose_name=b'Compiler / Preprocessor', choices=[(b'js', b'JS (None)'), (b'coffee', b'Coffeescript')])),
                ('created_by', models.ForeignKey(related_name='core_jsresource_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='core_jsresource_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', models.ForeignKey(to='core.JSPackage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LegacyURL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('uuid', models.CharField(help_text=b'UUID generated for object; can be used for short URLs', max_length=255, verbose_name='UUID', blank=True)),
                ('order', models.IntegerField(default=0, help_text=b'')),
                ('path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='path', blank=True)),
                ('title_path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True)),
                ('path_generated', models.CharField(help_text=b'The URL path to this page, based on page hierarchy and slug.', max_length=255, null=True, verbose_name='generated path', blank=True)),
                ('path_override', models.CharField(help_text=b'The URL path to this page, defined absolutely.', max_length=255, null=True, verbose_name='path override', blank=True)),
                ('hierarchy', models.CharField(null=True, max_length=255, blank=True, help_text=b'Administrative Hierarchy', unique=True, verbose_name='hierarchy')),
                ('temporary_redirect', models.CharField(help_text=b'Temporarily redirect to a different path', max_length=255, verbose_name='Temporary Redirect', blank=True)),
                ('permanent_redirect', models.CharField(help_text=b'Permanently redirect to a different path', max_length=255, verbose_name='Permanent Redirect', blank=True)),
                ('url', models.CharField(max_length=255, verbose_name='URL', db_index=True)),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
                ('created_by', models.ForeignKey(related_name='core_legacyurl_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='core_legacyurl_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LegacyURLReferer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('referer_title', models.CharField(help_text=b'', max_length=255, null=True, verbose_name='Referer Title', blank=True)),
                ('referer_url', models.CharField(help_text=b'', max_length=255, null=True, verbose_name='Referer URL', blank=True)),
                ('created_by', models.ForeignKey(related_name='core_legacyurlreferer_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('legacy_url', models.ForeignKey(to='core.LegacyURL')),
                ('modified_by', models.ForeignKey(related_name='core_legacyurlreferer_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('uuid', models.CharField(help_text=b'UUID generated for object; can be used for short URLs', max_length=255, verbose_name='UUID', blank=True)),
                ('order', models.IntegerField(default=0, help_text=b'')),
                ('path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='path', blank=True)),
                ('title_path', models.CharField(help_text=b'Actual path used based on generated and override path', max_length=255, null=True, verbose_name='title path', blank=True)),
                ('path_generated', models.CharField(help_text=b'The URL path to this page, based on page hierarchy and slug.', max_length=255, null=True, verbose_name='generated path', blank=True)),
                ('path_override', models.CharField(help_text=b'The URL path to this page, defined absolutely.', max_length=255, null=True, verbose_name='path override', blank=True)),
                ('hierarchy', models.CharField(null=True, max_length=255, blank=True, help_text=b'Administrative Hierarchy', unique=True, verbose_name='hierarchy')),
                ('temporary_redirect', models.CharField(help_text=b'Temporarily redirect to a different path', max_length=255, verbose_name='Temporary Redirect', blank=True)),
                ('permanent_redirect', models.CharField(help_text=b'Permanently redirect to a different path', max_length=255, verbose_name='Permanent Redirect', blank=True)),
                ('publication_date', models.DateTimeField(null=True, verbose_name='Publication Date', blank=True)),
                ('publication_status', models.IntegerField(default=10, help_text=b'Current publication status', choices=[(10, 'Draft'), (20, 'Needs Review'), (100, 'Published'), (40, 'Unpublished')])),
                ('publish_on_date', models.DateTimeField(help_text=b"Object state will be set to 'Published' on this date.", null=True, verbose_name='Publish on Date', blank=True)),
                ('expire_on_date', models.DateTimeField(help_text=b"Object state will be set to 'Expired' on this date.", null=True, verbose_name='Expire on Date', blank=True)),
                ('target', models.CharField(default=b'_self', help_text=b'', max_length=255, verbose_name='Target', choices=[(b'_blank', '_blank'), (b'_self', '_self'), (b'_parent', '_parent'), (b'_top', '_top')])),
                ('css_classes', models.CharField(default=b'', max_length=255, blank=True, help_text=b'Extra css classes to add to the item', null=True, verbose_name='CSS Classes')),
                ('extra_attributes', models.CharField(default=b'', max_length=255, blank=True, help_text=b'Extra attributes to add to the item', null=True, verbose_name='Extra Attributes')),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
                ('created_by', models.ForeignKey(related_name='core_menuitem_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='core_menuitem_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='core.MenuItem', null=True)),
                ('published_by', models.ForeignKey(related_name='core_menuitem_published_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date', null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified Date', null=True)),
                ('admin_note', models.TextField(null=True, verbose_name='admin note', blank=True)),
                ('title', models.CharField(help_text=b'The display title for this object.', max_length=255, null=True, verbose_name='Title', blank=True)),
                ('slug', models.CharField(help_text=b'Auto-generated page slug for this object.', max_length=255, verbose_name='Slug', db_index=True, blank=True)),
                ('custom_template', models.TextField(help_text=b'Override html template file with a custom template.', null=True, verbose_name='custom template', blank=True)),
                ('file_template', models.CharField(choices=[(b'403.html', b'403'), (b'404.html', b'404'), (b'500.html', b'500'), (b'maintenance.html', b'Maintenance'), (b'admin/index_test.html', b'Admin - Index Test'), (b'debug_toolbar/base.html', b'Debug Toolbar - Base'), (b'debug_toolbar/panels/sql.html', b'Debug Toolbar - Panels - Sql'), (b'debug_toolbar/panels/templates.html', b'Debug Toolbar - Panels - Templates'), (b'page/page_detail.html', b'Page - Page Detail')], max_length=255, blank=True, help_text=b'Choose an existing html template file. This will be overwritten in custom template is filled in.', null=True, verbose_name='Template')),
                ('created_by', models.ForeignKey(related_name='core_template_created_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='core_template_modified_by', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['title'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='menuitem',
            name='template',
            field=models.ForeignKey(blank=True, to='core.Template', help_text=b'Template for view', null=True),
        ),
        migrations.AddField(
            model_name='legacyurl',
            name='template',
            field=models.ForeignKey(blank=True, to='core.Template', help_text=b'Template for view', null=True),
        ),
        migrations.AddField(
            model_name='adminsidebar',
            name='template',
            field=models.ForeignKey(blank=True, to='core.Template', help_text=b'Template for view', null=True),
        ),
        migrations.AddField(
            model_name='adminlink',
            name='parent',
            field=models.ForeignKey(blank=True, to='core.AdminSidebar', null=True),
        ),
        migrations.AddField(
            model_name='adminlink',
            name='template',
            field=models.ForeignKey(blank=True, to='core.Template', help_text=b'Template for view', null=True),
        ),
        migrations.AddField(
            model_name='adminapplink',
            name='template',
            field=models.ForeignKey(blank=True, to='core.Template', help_text=b'Template for view', null=True),
        ),
        migrations.AddField(
            model_name='adminappgroup',
            name='template',
            field=models.ForeignKey(blank=True, to='core.Template', help_text=b'Template for view', null=True),
        ),
    ]
