'''
before merging to main.py do not forget add path: `private.`
'''
from deck_code_decode import *
from deck.private.dbfId_to_id import *

def main(deck_name,deck_code):

    deck_hero_dbfId = deck_code_decode(deck_code)[0]
    deck_card_dbfId = deck_code_decode(deck_code)[1]

    deck_id_array = dbfIdToId(deck_hero_dbfId, deck_card_dbfId)

    html_print = deck_id_array[0] + '<br>' + deck_id_array[1][0][0] + ' x' + deck_id_array[1][0][1]

    print (html_print)

main('mage','AAECAZ8FCLMD8wX0Bd3+Ar2GA96GA+OGA/CJAwv6AdwD1wXPBq8HrAiWDcrDApGAA++GA9KKAwA=')

key = input('Press any key to quit')
quit()
