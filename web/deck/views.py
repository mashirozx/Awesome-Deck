from django.shortcuts import render

# Create your views here.
# Django
from django.http import HttpResponse

# private functions
from private.main import *

def index(request):
    deck_name = request.GET['name']
    deck_code = request.GET['code'].replace(" ", "+")

    output = main(deck_name,deck_code)

    return HttpResponse(output)
