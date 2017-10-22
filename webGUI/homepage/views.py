from django.shortcuts import render

def index(request):
    return render(request, 'homepage/home.html')

def signup(request):
	return render(reuest, 'homepage/signup.html')