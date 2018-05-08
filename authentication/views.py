# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from authentication.forms import UserForm

# Create your views here.

def login_page(request):
	if request.method == 'POST':
		username = request.POST['username'].split('@')[0]
		password = request.POST['password']
		if 'next' in request.POST:
			nextpage = request.POST['next']
		else:
			nextpage = '/'
		user = authenticate(username=username, password=password)
		msg = []
		context = {'msg': msg}
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect(nextpage)
			else:
				# Return a 'disabled account' error message
				msg.append('Username/Email address or Password Invalid')
				return render(request, 'authentication/login.html', context)
		else:
			msg.append('Username/Email address or Password Invalid')
			return render(request, 'authentication/login.html', context)

	html = 'authentication/login.html'
	return render(request, html)

def sign_up(request):

	registered = False

	if request.method =="POST":
		user_form = UserForm(data=request.POST)
		if user_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
		else:
			print(user_form.errors)
	else:
		user_form=UserForm()
	#return HttpResponse("Sign up beech")
	html= 'authentication/signup.html'
	return render(request,html,
	{'user_form':user_form, 'registered':registered})

def log_out(request):
	return HttpResponse("Log out beach")
