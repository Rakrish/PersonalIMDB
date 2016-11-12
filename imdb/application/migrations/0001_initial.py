# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=255, db_column='Type')),
                ('title', models.CharField(max_length=255, db_column='Title')),
                ('synopsis', models.CharField(max_length=500, null=True, db_column='Synopsis', blank=True)),
                ('imageurl', models.CharField(max_length=1000, db_column='ImageURL')),
                ('day', models.CharField(max_length=255, null=True, db_column='Day', blank=True)),
                ('time', models.CharField(max_length=255, null=True, db_column='Time', blank=True)),
            ],
            options={
                'db_table': 'Items',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=255, db_column='UserName')),
                ('email', models.CharField(max_length=255, db_column='Email')),
            ],
            options={
                'db_table': 'User',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserPreference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('genre', models.CharField(max_length=255, db_column='Genre')),
                ('type', models.CharField(max_length=255, db_column='Type')),
                ('other', models.CharField(max_length=255, null=True, db_column='Other', blank=True)),
                ('userid', models.ForeignKey(to='application.User')),
            ],
            options={
                'db_table': 'UserPreference',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
