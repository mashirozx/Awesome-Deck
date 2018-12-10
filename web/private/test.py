'''
before merging to main.py do not forget add path: `private.`
'''
from deck_code_decode import *
from dbfId_to_id import *

def main(deck_name,deck_code):

    deck_hero_dbfId = deck_code_decode(deck_code)[0]
    deck_card_dbfId = deck_code_decode(deck_code)[1]

    deck_id_array = dbfIdToId(deck_hero_dbfId, deck_card_dbfId)

    return deck_id_array

#main('mage','AAECAf0EBrQDyQPu9gLG+ALi+ALwiQMMuwKLA78DqwSWBYoHysMC6vYClf8C74ADyIcDyocDAA==')



key = input('Press any key to quit')
quit()
