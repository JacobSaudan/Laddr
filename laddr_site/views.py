# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .forms import ProfileForm
from .models import *
from .utility import update_psyche
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.timezone import now


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
	player_card_data = get_player_card(user_id)
	return JsonResponse(player_card_data)

def get_player_card(player_id):
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
	return player_card_data

def multiple_player_cards(request):
	ids = request.data.get('ids', [])
	pcds = []
	for id in ids:
		pcds.append(get_player_card(id))
	return JsonResponse(pcds)


def add_player_preference(request):
	primary_user_id = request.data.get('primary_user_id')
	comparison_user_id = request.data.get('comparison_user_id')
	accepted = request.data.get('accept')
	primary_profile = Profile.objects.get(user_id=primary_user_id)
	comparison_profile = Profile.objects.get(user_id=comparison_user_id)
	ps = PsychePreference.create(
		user=primary_profile,
		potential_match=comparison_profile,
		date_created=now(),
		accepted=accepted,
	)
	ps.save()
	update_psyche(primary_profile)

def get_profile_information(request):
	if request.method == "POST":
		form = ProfileForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/')
	else:
		form = ProfileForm()
	
	return render(request, 'laddr_site/get_profile.html', {'form': form})


