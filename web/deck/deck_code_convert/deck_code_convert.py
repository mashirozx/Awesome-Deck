from hearthstone.deckstrings import Deck
from hearthstone.enums import FormatType

# See:
# https://hearthsim.info/docs/deckstrings/

def deckCodeConvertor(deck_code)
    deck = Deck.from_deckstring(deck_code)
    dack_data = [deck.heroes, deck.cards]
    return dack_data
