# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from .timezones import TIMEZONE_CHOICES

# Create your models here.

LOL_SERVERS = (
	('NA', 'North America'),
)

PLAYSTYLES = (
	('Aggressive', 'Aggressive'),
	('Conservative', 'Conservative'),
	('Supporting', 'Supporting'),
)

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    summoner_name = models.CharField(max_length=50, null=True, blank=False)
    lol_server = models.CharField(max_length=10, blank=False, choices=LOL_SERVERS, default='NA')
    timezones = models.CharField(max_length=40, default='Etc/UTC', choices=TIMEZONE_CHOICES)
    playstyle = models.CharField(max_length=40, choices=PLAYSTYLES, default='Conservative')
    availability = JSONField(default={
			'Monday': False,
			'Tuesday': False,
			'Wednesday': False,
			'Thursday': False,
			'Friday': False,
			'Saturday': False,
			'Sunday': False
		})


    def __str__(self):
    	return self.user.username

class Membership(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    date_joined = models.DateField()

class Team(models.Model):
	name = models.CharField(max_length=128)
	date_created = models.DateField()
	members = models.ManyToManyField(User, through='Membership')

	def __str__(self):
		return "%s : %s" % (self.name)

class Availability(models.Model):
	start = models.DateTimeField()
	end = models.DateTimeField()

	def __str__(self):
		date_format = "%A %H:%M"
		return "%s - %s" % (start.strftime(date_format), end.strftime(date_format))

class NewsBlurb(models.Model):
	
	# A model for landing/home page cards
	
	text = models.TextField(max_length=500)
	date_created = models.DateField()
	date_posted = models.DateField()
	date_removed = models.DateField()
	active = models.BooleanField(default=False)
	in_rotation = models.BooleanField(default=False)
	is_primary = models.BooleanField(default=False) # Marks Large primary card on landing





