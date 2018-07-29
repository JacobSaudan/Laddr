# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from .forms import ProfileForm
from .models import *
from .utility import (
    get_player_card, 
    get_team_info,
    get_team_member_ids,
    update_psyche, 
)
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
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
    data = json.loads(request.body)
    user_id = data.get('user_id', None)
    if user_id == None:
        return JsonResponse({
            "error_msg": "Expected user_id in request, got None instead",
            "success": False,
        })
    player_card_data = get_player_card(user_id)
    return JsonResponse({'success': True, 'data': player_card_data})

def multiple_player_cards(request):
    data = json.loads(request.body)
    ids = data.get('ids', [])
    pcds = []
    for id in ids:
        pcds.append(get_player_card(id))
    return JsonResponse({"success": True, "data": pcds})


def get_profile_information(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = ProfileForm()
    return render(request, 'laddr_site/get_profile.html', {'form': form})

def team_card_view(request):
    data = json.loads(request.body)
    team_id = data.get("team_id", None)
    if team_id == None:
        return JsonResponse({
            "error": "Expected team_id in request, got None instead",
            "success": False,
        })
    player_ids = get_team_member_ids(team_id)
    player_cards = [get_player_card(pid) for pid in player_ids]
    team_info = get_team_info(team_id)
    data = {
        "player_cards": player_cards,
        "team_info": team_info,
    }
    response = {
        "success": True,
        "data": data,
    }
    return JsonResponse(response)


def add_player_preference(request):
    data = json.loads(request.body)
    primary_user_id = data.get('primary_user_id')
    comparison_user_id = data.get('comparison_user_id')
    accepted = data.get('accept')
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
    return JsonResponse({"success": True})
