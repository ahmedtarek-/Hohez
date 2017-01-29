from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return HttpResponse("<h1>Hello there captain Hohez\n</h1> <a href='/rango/about'> About</a>")


def about(request):
	return HttpResponse("<h1> ALL ABOUT US, THE HOHEZ </h2> <a href='/rango'> Home</a>")