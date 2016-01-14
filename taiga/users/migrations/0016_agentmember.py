# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20151221_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('agentid', models.ForeignKey(related_name='user_agent', to=settings.AUTH_USER_MODEL)),
                ('memberid', models.ForeignKey(related_name='user_member', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'agentmember',
                'verbose_name_plural': 'agentmembers',
            },
        ),
    ]
