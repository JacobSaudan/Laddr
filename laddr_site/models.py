# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from .timezones import TIMEZONE_CHOICES

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.ManyToManyField('Game', through='PlayerGame')
    timezones = models.CharField(max_length=40, default='Etc/UTC', choices=TIMEZONE_CHOICES)

    def __str__(self):
    	return self.user.username

class Membership(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    date_joined = models.DateField()

class Team(models.Model):
	name = models.CharField(max_length=128)
	game = models.ForeignKey('Game', on_delete=models.CASCADE)
	date_created = models.DateField()
	members = models.ManyToManyField(User, through='Membership')

	def __str__(self):
		return "%s : %s" % (self.name, self.game)

class Availability(models.Model):
	game = models.ForeignKey('Game', on_delete=models.CASCADE)
	start = models.DateTimeField()
	end = models.DateTimeField()

	def __str__(self):
		date_format = "%A %H:%M"
		return "%s: %s - %s" % (game.title, start.strftime(date_format), end.strftime(date_format))



class Game(models.Model):
	title = models.CharField(max_length=128)
	team_size = models.IntegerField(null=True)

	def __str__(self):
		return self.title

class Tournament_Game(models.Model):
	team_1 = models.ForeignKey('Team', related_name='%(class)s_1', on_delete=models.CASCADE)
	team_2 = models.ForeignKey('Team', related_name='%(class)s_2', on_delete=models.CASCADE)
	scheduled_date = models.DateTimeField(null=False, blank=False)
	completed = models.BooleanField(default=False)
	tournament = models.ForeignKey('Tournament', null=True, on_delete=models.CASCADE)

	def __str__(self):
		return "%s vs. %s - %s" % (team_1.name, team_2.name, scheduled_date.strftime("%m/%d/%y %H:%M"))

	class Meta:
		unique_together = (('team_1', 'team_2'),)


class PlayerGame(models.Model):
	PLAYSTYLES = (
		('Aggressive', 'Aggressive'),
		('Conservative', 'Conservative'),
		('Supporting', 'Supporting')
	)
	AVAILABILITIES = (
		('Morning', 'Morning'),
		('Afternoon', 'Afternoon'),
		('Everning', 'Everning'),
		('Late Night', 'Late Night')
	)
	WEEKDAYS = (
		('Monday', 'Monday'),
		('Tuesday', 'Tuesday'),
		('Wednesday', 'Wednesday'),
		('Thursday', 'Thursday'),
		('Friday', 'Friday'),
		('Saturday', 'Saturday'),
		('Sunday', 'Sunday'),
	)
	user_profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
	game = models.ForeignKey('Game', on_delete=models.CASCADE)
	playstyle = models.CharField(max_length=40, choices=PLAYSTYLES)
	is_favorite = models.BooleanField(default=False)
	availability_time = models.CharField(max_length=40, choices=AVAILABILITIES)
	availability_day = models.CharField(max_length=10, choices=WEEKDAYS)

	class Meta:
		unique_together = (('user_profile', 'is_favorite'),) # A player can only have one favorite game

	def __str__(self):
		return "%s : %s" % (self.user_profile.user.username, self.game.title)

class Tournament(models.Model):
	game = models.ForeignKey('Game', on_delete=models.CASCADE)
	Teams = models.ManyToManyField('Team')

class NewsBlurb(models.Model):
	
	# A model for landing/home page cards
	
	text = models.TextField(max_length=500)
	date_created = models.DateField()
	date_posted = models.DateField()
	date_removed = models.DateField()
	active = models.BooleanField(default=False)
	in_rotation = models.BooleanField(default=False)
	is_primary = models.BooleanField(default=False) # Marks Large primary card on landing





