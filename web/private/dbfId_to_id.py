'''
convert a deck series of dbfId to a series of idea
[435,[...]] => [EX1_365,[...]]
'''
import MySQLdb
import json
import os

def sqlFind(dbfId):
    '''
    TODO:
    better to read these parameters from a conf file
    '''
    host='localhost'
    user='root'
    passwd='password'
    db='hearthstone'
    table_name='cards_data_27845'

    db = MySQLdb.connect(host, user, passwd, db, use_unicode=True, charset="utf8")
    cursor = db.cursor()

    sql = "SELECT * FROM " + table_name + " WHERE hs_dbfId = %s" % (dbfId) #435
    try:
       cursor.execute(sql)
       results = cursor.fetchall()

       card_id = results[0][2]
       card_name = results[0][3]
       card_cost = results[0][4]
       card_rarity = results[0][5]

    except:
       print ("Error: unable to fecth data")

    db.close()
    # Formate: {'id': card_id, 'name': card_name, 'cost': card_cost, 'rarity': card_rarity}
    return [card_id, card_name, card_cost, card_rarity]

def dbfIdToId(deck_hero_dbfId, deck_card_dbfId):
    hero = sqlFind(deck_hero_dbfId)

    deck = {}
    deck_cards = []
    max_cost = 0

    for card in deck_card_dbfId:
        # formate [(id,num,name,cost,rarity),...]
        this_sql = sqlFind(card[0])
        deck_cards.append((this_sql[0],card[1],this_sql[1],this_sql[2],this_sql[3]))
        if this_sql[2] > max_cost:
            max_cost = this_sql[2]

    # hero info, formate: [id,name]
    deck["hero"] = [hero[0],hero[1]]
    deck["cards"] = deck_cards
    deck["max_cost"] = max_cost
    return deck


deck = [(435, 1), (755, 1), (756, 1), (48989, 1), (49981, 1), (50014, 1), (50019, 1), (50416, 1), (250, 2), (476, 2), (727, 2), (847, 2), (943, 2), (1068, 2), (1686, 2), (41418, 2), (49169, 2), (50031, 2), (50514, 2)]
hero = 671

print (str(dbfIdToId(hero,deck)))
