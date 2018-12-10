from hearthstone.deckstrings import Deck
from hearthstone.enums import FormatType

def deck_code_decode(deck_code):
    # Deckstring decode. See:
    # https://hearthsim.info/docs/deckstrings/
    deck = Deck.from_deckstring(deck_code)
    deck_hero = deck.heroes[0]
    deck_card = deck.cards

    return [deck_hero, deck_card]
