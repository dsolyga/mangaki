# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-09 19:44
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.postgres.operations import CreateExtension, UnaccentExtension


class Migration(migrations.Migration):

    dependencies = [
        ('mangaki', '0001_squashed_0054_merge'),
    ]

    operations = [
            UnaccentExtension(),
            CreateExtension('pg_trgm'),
            migrations.RunSQL("""
            CREATE OR REPLACE FUNCTION F_UNACCENT(text) RETURNS text AS
            $func$
            SELECT public.unaccent('public.unaccent', $1)
            $func$ LANGUAGE sql IMMUTABLE;
            CREATE INDEX mangaki_search_work_upper ON mangaki_work USING gist(UPPER(F_UNACCENT(title)) gist_trgm_ops);
            """,
            """
            DROP INDEX mangaki_search_work_upper;
            DROP FUNCTION F_UNACCENT(text);
            """
            ),
    ]
