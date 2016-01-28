# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_user_agent1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agentmember',
            name='agentid',
        ),
        migrations.RemoveField(
            model_name='agentmember',
            name='memberid',
        ),
        migrations.DeleteModel(
            name='AgentMember',
        ),
    ]
