from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'index.html', {'name': 'Wilson'})

def home(request):
	return render(request, 'web/home.html', {'page': 'home'})

def planejamento(request):
	return render(request, 'web/planejamento.html', {'page': 'planejamento'})