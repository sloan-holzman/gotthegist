# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Matatus(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ratings = models.CharField(db_column='Ratings', max_length=45, blank=True)  # Field name made lowercase.
    number_of_comments = models.CharField(max_length=45, blank=True)
    plate_number = models.CharField(max_length=45, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matatus'


class Reviews(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    route_shot_name = models.CharField(max_length=45, blank=True)
    id_user = models.CharField(max_length=45, blank=True)
    plate_number = models.CharField(max_length=45, blank=True)
    rating = models.CharField(db_column='Rating', max_length=45, blank=True)  # Field name made lowercase.
    comments = models.CharField(max_length=2000, blank=True)
    date = models.DateTimeField(blank=True, null=True)
    comment_number = models.CharField(max_length=45, blank=True)
    comment_title = models.CharField(max_length=1000, blank=True)
    username = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'reviews'


class Routes(models.Model):
    route_id = models.CharField(max_length=11, blank=True)
    agency_id = models.CharField(max_length=3, blank=True)
    route_shot_name = models.CharField(max_length=45, blank=True)
    route_long_name = models.CharField(max_length=45, blank=True)
    route_desc = models.CharField(max_length=45, blank=True)
    route_type = models.CharField(max_length=45, blank=True)
    route_url = models.CharField(max_length=45, blank=True)
    route_color = models.CharField(max_length=45, blank=True)
    route_text_color = models.CharField(max_length=45, blank=True)
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'routes'


class Stops(models.Model):
    stop_id = models.CharField(primary_key=True, max_length=7)
    stop_code = models.CharField(max_length=45, blank=True)
    stop_name = models.CharField(max_length=45, blank=True)
    stop_lat = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    stop_lon = models.DecimalField(max_digits=8, decimal_places=6, blank=True, null=True)
    zone_id = models.CharField(max_length=45, blank=True)
    stop_url = models.CharField(max_length=45, blank=True)
    location_type = models.CharField(max_length=45, blank=True)
    parent_station = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'stops'


class Users(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    username = models.CharField(unique=True, max_length=255)
    hash = models.CharField(max_length=255)
    email = models.CharField(max_length=45, blank=True)
    phone = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'users'
