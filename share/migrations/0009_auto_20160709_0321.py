# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 03:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0008_auto_20160709_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractcreativeworkversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='affiliationversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='associationversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='awardversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='change',
            name='node_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contributorversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='emailversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='entityversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='extradataversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='identifierversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='link',
            name='type',
            field=models.TextField(choices=[('doi', 'DOI'), ('provider', 'Provider'), ('misc', 'Miscellaneous')]),
        ),
        migrations.AlterField(
            model_name='linkversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='linkversion',
            name='type',
            field=models.TextField(choices=[('doi', 'DOI'), ('provider', 'Provider'), ('misc', 'Miscellaneous')]),
        ),
        migrations.AlterField(
            model_name='personemailversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='personversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='rawdata',
            name='provider_doc_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='rawdata',
            name='sha256',
            field=models.TextField(validators=[django.core.validators.MaxLengthValidator(64)]),
        ),
        migrations.AlterField(
            model_name='shareuser',
            name='first_name',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(64)], verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='shareuser',
            name='last_name',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(64)], verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='shareuser',
            name='locale',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(100)]),
        ),
        migrations.AlterField(
            model_name='shareuser',
            name='long_title',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(100)]),
        ),
        migrations.AlterField(
            model_name='shareuser',
            name='robot',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(40)]),
        ),
        migrations.AlterField(
            model_name='shareuser',
            name='time_zone',
            field=models.TextField(blank=True, validators=[django.core.validators.MaxLengthValidator(100)]),
        ),
        migrations.AlterField(
            model_name='shareuser',
            name='username',
            field=models.TextField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, validators=[django.core.validators.MaxLengthValidator(64), django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='tagversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='throughawardsversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='throughidentifiersversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='throughlinksversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='throughtagsversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='throughvenuesversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='venueversion',
            name='action',
            field=models.TextField(max_length=10),
        ),
    ]
