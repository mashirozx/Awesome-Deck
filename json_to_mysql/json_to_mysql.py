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

def jsonToMySQL(host, user, passwd, db, table_name, json_file):
    #link db
    db = MySQLdb.connect(host, user, passwd, db, use_unicode=True, charset="utf8")
    cursor = db.cursor()

    #delete already exist table
    cursor.execute("DROP TABLE IF EXISTS " + table_name)

    #create table
    sql_create_table = '''CREATE TABLE ''' + table_name + ''' (
             hs_jsonId INT,
             hs_dbfId INT,
             hs_id VARCHAR(225),
             hs_name VARCHAR(225)) DEFAULT CHARSET=utf8'''

    cursor.execute(sql_create_table)

    with open(json_file, 'r', encoding='UTF-8') as f:
        json_data = json.load(f)

    print (len(json_data))

    for i in range(0, len(json_data), 1):
        if 'dbfId' not in json_data[i] or 'name' not in json_data[i] or 'id' not in json_data[i]:
            print("data missing: jsonId="+str(i))
            continue

        data_jsonId = str(i)
        data_dbfId = str(json_data[i]['dbfId']) # 2539
        data_id = json_data[i]['id']            # AT_001
        data_name = json_data[i]['name']        # 炎枪术
        sql_pre_value = '(' + data_jsonId + ',' + data_dbfId + ',"' + data_id + '","' + data_name + '")'
        print (sql_pre_value)
        sql_insert = '''INSERT INTO ''' + table_name + '''(hs_jsonId, hs_dbfId, hs_id, hs_name) VALUES ''' + sql_pre_value

        try:
           # 执行sql语句
           cursor.execute(sql_insert)
           # 提交到数据库执行
           db.commit()
           print('ok')
        except:
           # Rollback in case there is any error
           db.rollback()
           print('err: jsonId=' + data_jsonId)
           print (sql_insert)

    #disconnect db
    db.close()

    print('Done.')
