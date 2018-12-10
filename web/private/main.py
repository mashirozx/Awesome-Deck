from deck.private.deck_code_decode import *
from deck.private.dbfId_to_id import *

def main(deck_name,deck_code):

    html_print = str(deck_code_decode(deck_code)[0])+'<br>'+deck_code

    return html_print
