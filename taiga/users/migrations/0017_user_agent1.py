# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_agentmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='agent1',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='agent1', related_name='user', null=True),
        ),
    ]
