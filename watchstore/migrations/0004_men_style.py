# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchstore', '0003_auto_20160413_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='men',
            name='style',
            field=models.CharField(default='', max_length=10, choices=[(b'Casual', b'Casual'), (b'Sporty', b'Sporty')]),
            preserve_default=False,
        ),
    ]
