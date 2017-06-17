# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
	if 'counter' not in request.session:
		request.session['counter'] = 0
	random = get_random_string(length=42)
	info = {
		'random_word': random,
	}
	return render(request, 'random_word/index.html', info)

def generate(request):
	if request.method == "POST":
		request.session['counter'] += 1
		return redirect('/')
	else:
		return redirect('/')
