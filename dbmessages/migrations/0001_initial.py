# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(help_text=b'A number. The values for the built-in levels are:<table><tr><th>Level Constant<th>Value<tr><td>DEBUG   <td>10<tr><td>INFO    <td>20<tr><td>SUCCESS <td>25<tr><td>WARNING <td>30<tr><td>ERROR   <td>40</table>')),
                ('message', models.TextField(default=b'')),
                ('extra_tags', models.TextField(default=b'', help_text=b'Space-separated words.', blank=True)),
                ('to_user', models.ForeignKey(related_name='dbmessages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
