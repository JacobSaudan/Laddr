# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.ManyToManyField('Game', through='PlayerGame')
    availability = models.ManyToManyField('Availability')


    def __str__(self):
    	return self.user.username

class Availability(models.Model):
	game = models.ForeignKey('Game', on_delete=models.CASCADE)
	start = models.DateTimeField()
	end = models.DateTimeField()

	def __str__(self):
		date_format = "%A %H:%M"
		return "%s: %s - %s" % (game.title, start.strftime(date_format), end.strftime(date_format))

class Team(models.Model):
	name = models.CharField(max_length=128)
	game = models.ForeignKey('Game')
	date_created = models.DateField()
	members = models.ManyToManyField(User, through='Membership')

	def __str__(self):
		return "%s : %s" % (self.name, self.game)

class Game(models.Model):
	title = models.CharField(max_length=128)
	team_size = models.IntegerField(null=True)

	def __str__(self):
		return self.title

class Tournament_Game(models.Model):
	team_1 = models.ForeignKey('Team', related_name='%(class)s_1')
	team_2 = models.ForeignKey('Team', related_name='%(class)s_2')
	scheduled_date = models.DateTimeField(null=False, blank=False)
	completed = models.BooleanField(default=False)
	tournament = models.ForeignKey('Tournament', null=True)

	def __str__(self):
		return "%s vs. %s - %s" % (team_1.name, team_2.name, scheduled_date.strftime("%m/%d/%y %H:%M"))

	class Meta:
		unique_together = (('team_1', 'team_2'),)


class Membership(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_joined = models.DateField()

class PlayerGame(models.Model):
	PLAYSTYLES = (
		('Aggressive', 'Aggressive'),
		('Conservative', 'Conservative'),
		('Supporting', 'Supporting')
	)
	user_profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
	game = models.ForeignKey('Game', on_delete=models.CASCADE)
	playstyle = models.CharField(max_length=40, choices=PLAYSTYLES)


	def __str__(self):
		return "%s : %s" % (self.user_profile.user.username, self.game.title)

class Tournament(models.Model):
	game = models.ForeignKey('Game')
	Teams = models.ManyToManyField('Team')




