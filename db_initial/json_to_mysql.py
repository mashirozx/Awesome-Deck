#coding=utf-8
'''
Created on 2018-12-10
Update  on 2018-12-10
@author: Mashiro @ https://2heng.xin

Desc: Convert Hearthstone cards data to MySQL.
'''

import MySQLdb
import json
import os
import requests

def jsonToMySQL(host, user, passwd, db_name, table_name):
    json_url = 'https://api.hearthstonejson.com/v1/latest/zhCN/cards.json'
    json_response = requests.get(json_url)
    #print (response.text)
    json_data = json_response.json()

    #link db
    db = MySQLdb.connect(host, user, passwd, db_name, use_unicode=True, charset="utf8")
    cursor = db.cursor()

    #delete already exist table
    cursor.execute("DROP TABLE IF EXISTS " + table_name)

    #create table
    sql_create_table = '''CREATE TABLE ''' + table_name + ''' (
             hs_jsonId INT,
             hs_dbfId INT,
             hs_id VARCHAR(225),
             hs_name VARCHAR(225),
             hs_cost INT,
             hs_rarity VARCHAR(225)) DEFAULT CHARSET=utf8'''

    header_tag_list = ('dbfId','id','name','cost','rarity')
    char_type_tags = ('id', 'name', 'rarity')

    cursor.execute(sql_create_table)

    #with open(json_file, 'r', encoding='UTF-8') as f:
    #    json_data = json.load(f)

    print (len(json_data))

    for i in range(0, len(json_data), 1):
    #for i in range(0, 10, 1):
        '''
        if 'dbfId' not in json_data[i] or 'name' not in json_data[i] or 'id' not in json_data[i]:
            print("data missing: jsonId="+str(i))
            continue
        '''
        data = {'id': i}
        for header_tag in header_tag_list:
            if header_tag in json_data[i]:
                data[header_tag] = str(json_data[i][header_tag])

        sql_pre_key = '(hs_jsonId'
        sql_pre_value = '(' + str(i)
        for key, value in data.items():
            sql_pre_key = sql_pre_key + ', hs_' + key
            if key in char_type_tags:
                sql_pre_value = sql_pre_value + ', "' + value + '"'
            else:
                sql_pre_value = sql_pre_value + ', ' + value
        sql_pre_key = sql_pre_key + ')'
        sql_pre_value = sql_pre_value + ')'

        '''
        data_jsonId = str(i)
        data_dbfId = str(json_data[i]['dbfId']) # 2539
        data_id = json_data[i]['id']            # AT_001
        data_name = json_data[i]['name']        # 炎枪术
        '''
        sql_insert = '''INSERT INTO ''' + table_name + sql_pre_key + ''' VALUES ''' + sql_pre_value
        print (sql_insert)

        try:
           # 执行sql语句
           cursor.execute(sql_insert)
           # 提交到数据库执行
           db.commit()
           print('ok')
        except:
           # Rollback in case there is any error
           db.rollback()
           print('err: jsonId=' + str(i))
           print (sql_insert)

    #disconnect db
    db.close()

    print('Done.')
