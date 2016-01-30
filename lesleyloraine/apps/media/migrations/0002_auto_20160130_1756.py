# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import carbon.atoms.models.media
import lesleyloraine.s3utils


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(help_text=b'To ensure a precise color replication in image variants, make sure an sRGB color profile has been assigned to each image.', storage=lesleyloraine.s3utils._MediaS3BotoStorage(bucket=b'lesleyloraine-dev', custom_domain=b'lesleyloraine-dev.s3.amazonaws.com', location=b'media'), null=True, upload_to=carbon.atoms.models.media.image_file_name, blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(storage=lesleyloraine.s3utils._MediaS3BotoStorage(bucket=b'lesleyloraine-dev', custom_domain=b'lesleyloraine-dev.s3.amazonaws.com', location=b'media'), null=True, upload_to=carbon.atoms.models.media.media_file_name, blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='image',
            field=models.ImageField(help_text=b'To ensure a precise color replication in image variants, make sure an sRGB color profile has been assigned to each image.', storage=lesleyloraine.s3utils._MediaS3BotoStorage(bucket=b'lesleyloraine-dev', custom_domain=b'lesleyloraine-dev.s3.amazonaws.com', location=b'media'), null=True, upload_to=carbon.atoms.models.media.image_file_name, blank=True),
        ),
    ]
