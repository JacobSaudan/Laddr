# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import *


# Create your views here.

def landing_page(request):
	html = 'laddr_site/landing.html'
	return render(request, html)

def home_page(request):
	html = 'laddr_site/home.html'
	return render(request, html)

def teams_page(request):
	html = 'laddr_site/teams.html'
	return render(request, html)

def compete_page(request):
	html = 'laddr_site/compete.html'
	return render(request, html)

def profile_page(request):
	html = 'laddr_site/profile.html'
	user = request.user
	context = {
		"user_name": user,
		"tournaments": user.tournament_set.all(),
		"games": user.game_set.all(),
		"teams": user.team_set.all()
	}
	return render(request, html, context=context)

def store_page(request):
	html = 'laddr_site/store.html'
	return render(request, html)

def find_team(request):
	html = 'laddr_site/find_team.html'
	return render(request, html)

def articles(request):
	html = 'laddr_site/articles.html'
	return render(request, html)

def events(request):
	html = 'laddr_site/events.html'
	return render(request, html)

def patch_notes(request):
	html = 'laddr_site/patch_notes.html'
	return render(request, html)

def player_card_data(request):
	user_id = request.GET.get('user_id', 1)
	user = User.objects.get(id=user_id)
	profile = Profile.objects.get(user=user)
	player_card_data = {
		'user_name': user.username,
		'summoner_name': profile.summoner_name,
		'server': profile.lol_server,
		'top_champions': profile.top_champions,
		'bio': profile.bio,
		'rank': profile.rank,
		'role': profile.role,
		'psyche': profile.get_psyche(),
		'header_color': profile.favorite_color,
	}
	return JsonResponse(player_card_data)


