from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(db_column='UserName', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'User'

class UserPreference(models.Model):
    userid = models.ForeignKey("User")  # Field name made lowercase.    
    genre = models.CharField(db_column='Genre', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255)  # Field name made lowercase.
    other = models.CharField(db_column='Other', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'UserPreference'

class Items(models.Model):
    type = models.CharField(db_column='Type', max_length=255)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=255)  # Field name made lowercase.
    synopsis = models.CharField(db_column='Synopsis', max_length=500, blank=True, null=True)  # Field name made lowercase.
    imageurl = models.CharField(db_column='ImageURL', max_length=1000)  # Field name made lowercase.
    day = models.CharField(db_column='Day', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Items'

class Subscribers(models.Model):
    userid = models.ForeignKey("User")  # Field name made lowercase. 
    item = models.ForeignKey("Items")  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Subscribers'
