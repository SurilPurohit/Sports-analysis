from django.shortcuts import render
from django.http import HttpResponse

def foot(request):
	return HttpResponse("Hello World Football")    
    # return render(request, 'index.html', {})