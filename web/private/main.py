'''
before merging to main.py do not forget add path: `private.`
'''

'''
before merging to main.py do not forget add path: `private.`
'''
from private.deck_code_decode import *
from private.dbfId_to_id import *
from private.deck_html_generator import *

def main(deck_name,deck_code):

    deck_hero_dbfId = deck_code_decode(deck_code)[0]
    deck_card_dbfId = deck_code_decode(deck_code)[1]

    deck_id_array = dbfIdToId(deck_hero_dbfId, deck_card_dbfId)

    #return str(deck_id_array)
    return generate_html(deck_id_array, deck_code, lang="zhCN", deck_name = deck_name)

#t= main('mage','AAECAf0EBrQDyQPu9gLG+ALi+ALwiQMMuwKLA78DqwSWBYoHysMC6vYClf8C74ADyIcDyocDAA==')

#print (t)

"""
def main(deck_name,deck_code):

    html_print = '''<body><img src="/static/img.jpg"></body>'''
    return html_print
"""
