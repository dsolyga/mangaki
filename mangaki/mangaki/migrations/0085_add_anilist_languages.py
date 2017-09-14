# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-25 13:58
from __future__ import unicode_literals

from django.db import migrations


def add_languages(apps, schema):
    Language = apps.get_model('mangaki', 'Language')
    ExtLanguage = apps.get_model('mangaki', 'ExtLanguage')

    db_alias = schema.connection.alias
    lang_model_map = {lang.code: lang for lang in Language.objects.all()}

    ExtLanguage.objects.using(db_alias).bulk_create([
        ExtLanguage(source='anilist', ext_lang='romaji',
                    lang=lang_model_map['x-jat']),
        ExtLanguage(source='anilist', ext_lang='english',
                    lang=lang_model_map['en']),
        ExtLanguage(source='anilist', ext_lang='japanese',
                    lang=lang_model_map['ja']),
        ExtLanguage(source='anilist', ext_lang='unknown',
                    lang=lang_model_map[None])
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('mangaki', '0084_add_origin_suggestion_to_workcluster'),
    ]

    operations = [
        migrations.RunPython(add_languages)
    ]
