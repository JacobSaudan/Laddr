# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    games = models.ManyToManyField(Game)

class Team(models.Model):
	name = models.CharField(max_length=128)
	date_created = model.DateField()
	members = models.ManyToManyField(User, through='Membership')

class Membership(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_joined = models.DateField()

class Game(models.Model):
	title = models.CharField(max_length=128)