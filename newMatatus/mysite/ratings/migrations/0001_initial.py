# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField()),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=75)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Matatus',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('ratings', models.CharField(max_length=45, db_column='Ratings', blank=True)),
                ('number_of_comments', models.CharField(max_length=45, blank=True)),
                ('plate_number', models.CharField(max_length=45, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=9, decimal_places=6, blank=True)),
                ('latitude', models.DecimalField(null=True, max_digits=9, decimal_places=6, blank=True)),
            ],
            options={
                'db_table': 'matatus',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('route_shot_name', models.CharField(max_length=45, blank=True)),
                ('id_user', models.CharField(max_length=45, blank=True)),
                ('plate_number', models.CharField(max_length=45, blank=True)),
                ('rating', models.CharField(max_length=45, db_column='Rating', blank=True)),
                ('comments', models.CharField(max_length=2000, blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('comment_number', models.CharField(max_length=45, blank=True)),
                ('comment_title', models.CharField(max_length=1000, blank=True)),
                ('username', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'db_table': 'reviews',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('route_id', models.CharField(max_length=11, blank=True)),
                ('agency_id', models.CharField(max_length=3, blank=True)),
                ('route_shot_name', models.CharField(max_length=45, blank=True)),
                ('route_long_name', models.CharField(max_length=45, blank=True)),
                ('route_desc', models.CharField(max_length=45, blank=True)),
                ('route_type', models.CharField(max_length=45, blank=True)),
                ('route_url', models.CharField(max_length=45, blank=True)),
                ('route_color', models.CharField(max_length=45, blank=True)),
                ('route_text_color', models.CharField(max_length=45, blank=True)),
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'routes',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stops',
            fields=[
                ('stop_id', models.CharField(max_length=7, serialize=False, primary_key=True)),
                ('stop_code', models.CharField(max_length=45, blank=True)),
                ('stop_name', models.CharField(max_length=45, blank=True)),
                ('stop_lat', models.DecimalField(null=True, max_digits=8, decimal_places=6, blank=True)),
                ('stop_lon', models.DecimalField(null=True, max_digits=8, decimal_places=6, blank=True)),
                ('zone_id', models.CharField(max_length=45, blank=True)),
                ('stop_url', models.CharField(max_length=45, blank=True)),
                ('location_type', models.CharField(max_length=45, blank=True)),
                ('parent_station', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'db_table': 'stops',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=255)),
                ('hash', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=45, blank=True)),
                ('phone', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
