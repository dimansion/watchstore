# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchstore', '0002_men_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='men',
            name='desc',
            field=models.TextField(max_length=200, null=True, blank=True),
        ),
    ]
