# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.ManyToManyField('Game')

    def __str__(self):
    	return self.user.username

class Team(models.Model):
	name = models.CharField(max_length=128)
	game = models.ForeignKey('Game')
	date_created = models.DateField()
	members = models.ManyToManyField(User, through='Membership')

	def __str__(self):
		return "%s : %s" % (self.name, self.game)

class Membership(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_joined = models.DateField()

class Game(models.Model):
	title = models.CharField(max_length=128)
	team_size = models.IntegerField(null=True)

	def __str__(self):
		return self.title

class Bout(models.Model):
	team_1 = models.ForeignKey('Team', related_name='%(class)s_1')
	team_2 = models.ForeignKey('Team', related_name='%(class)s_2')
	date = models.DateField()

	class Meta:
		unique_together = (('team_1', 'team_2'),)