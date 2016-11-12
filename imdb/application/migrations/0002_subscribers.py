# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.ForeignKey(to='application.Items')),
                ('userid', models.ForeignKey(to='application.User')),
            ],
            options={
                'db_table': 'Subscribers',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
