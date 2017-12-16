# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

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