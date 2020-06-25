from django.shortcuts import render
from django.http import HttpResponse

def upcom(request):
	return HttpResponse("Hello World Upcoming")