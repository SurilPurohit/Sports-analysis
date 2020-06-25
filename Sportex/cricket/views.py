from django.shortcuts import render
from django.http import HttpResponse

def cric(request):
	return HttpResponse("Hello World Cricket")