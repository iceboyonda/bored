from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Django and Python Chat App</h1><iframe src="https://deadsimplechat.com/bBGV9utm_" width="100%" height="600px"></iframe>')