'''
convert a deck series of dbfId to a series of idea
[435,[...]] => [EX1_365,[...]]

input:
deck = [(435, 1), (755, 1), (756, 1), (48989, 1), (49981, 1), (50014, 1), (50019, 1), (50416, 1), (250, 2), (476, 2), (727, 2), (847, 2), (943, 2), (1068, 2), (1686, 2), (41418, 2), (49169, 2), (50031, 2), (50514, 2)]
hero = 671

return:
{
    "hero": [
        "HERO_04",
        "乌瑟尔·光明使者"
    ],
    'cards': [
        ('EX1_365', 1, '神圣愤怒', 5, 'RARE'),
        ('EX1_590', 1, '血骑士', 3, 'EPIC'),
        ('EX1_619', 1, '生而平等', 2, 'RARE'),
        ('BOT_910', 1, '亮石技师', 6, 'EPIC'),
        ('TRL_300', 1, '西瓦尔拉，猛虎之神', 25, 'LEGENDARY'),
        ('TRL_304', 1, '法拉基战斧', 5, 'RARE'),
        ('TRL_305', 1, '新人登场', 7, 'EPIC'),
        ('TRL_528', 1, '阵 线破坏者', 7, 'EPIC'),
        ('CS2_094', 2, '愤怒之锤', 4, 'FREE'),
        ('CS2_093', 2, '奉献', 4, 'FREE'),
        ('EX1_371', 2, '保护之 手', 1, 'FREE'),
        ('CS2_097', 2, '真银圣剑', 4, 'FREE'),
        ('CS2_092', 2, '王者祝福', 4, 'FREE'),
        ('CS2_088', 2, '列王守卫', 7, 'FREE'),
        ('CS2_200', 2, '石拳食人魔', 6, 'FREE'),
        ('UNG_928', 2, '焦油爬行者', 3, 'COMMON'),
        ('BOT_537', 2, '机械蛋', 5, 'COMMON'),
        ('TRL_309', 2, '猛虎之灵', 4, 'RARE'),
        ('TRL_545', 2, '赞达拉武士', 4, 'RARE')
    ],
    "max_cost": 25
}


'''
import MySQLdb
import json
import os
import configparser

def sqlFind(dbfId):
    config = configparser.ConfigParser()
    ## this path is only for single test!
    config.read('../../conf.ini')
    db_conf = config['DATABASE']
    host = db_conf['Host']
    user = db_conf['User']
    passwd = db_conf['Password']
    db_name = db_conf['Database']
    table_name = db_conf['TablePrefix'] + db_conf['HearthstoneVersion']

    db = MySQLdb.connect(host, user, passwd, db_name, use_unicode=True, charset="utf8")
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
        this_sql = sqlFind(card[0])
        #        formate [(    id,         num,       name,       cost,     rarity),...]
        deck_cards.append((this_sql[0], card[1], this_sql[1], this_sql[2], this_sql[3]))
        if this_sql[2] > max_cost:
            max_cost = this_sql[2]

    deck_cards_ordered = []
    rarity_tags = ["FREE", "COMMON", "RARE", "EPIC", "LEGENDARY"]
    for i in range(1, max_cost, 1):
        for t in rarity_tags:
            for x in deck_cards:
                if x[3] == i and x[4] == t:
                    deck_cards_ordered.append(x)

    # hero info, formate: [id,name]
    deck["hero"] = [hero[0],hero[1]]
    deck["cards"] = deck_cards_ordered
    return deck


#deck = [(435, 1), (755, 1), (756, 1), (48989, 1), (49981, 1), (50014, 1), (50019, 1), (50416, 1), (250, 2), (476, 2), (727, 2), (847, 2), (943, 2), (1068, 2), (1686, 2), (41418, 2), (49169, 2), (50031, 2), (50514, 2)]
#hero = 671

#print (str(dbfIdToId(hero,deck)))
