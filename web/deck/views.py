from django.shortcuts import render

# Create your views here.
# Django
from django.http import HttpResponse

# deck code convert
from hearthstone.deckstrings import Deck
from hearthstone.enums import FormatType

def index(request):
    deck_name = request.GET['name']
    deck_code = request.GET['code'].replace(" ", "+")
    
    # Deckstring decode. See:
    # https://hearthsim.info/docs/deckstrings/
    deck = Deck.from_deckstring(deck_code)
    deck_hero = deck.heroes[0]
    deck_card = deck.cards

    output = str(deck_hero)+'<br>'+deck_code

    return HttpResponse(output)
