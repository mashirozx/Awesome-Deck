from db_initial.json_to_mysql import *
import configparser
import schedule
import datetime
import time

# Conf Parser
config = configparser.ConfigParser()
config.read('conf.ini')
db_conf = config['DATABASE']

host = db_conf['Host']
user = db_conf['User']
passwd = db_conf['Password']
db_name = db_conf['Database']
table_name = db_conf['TableName']

def job():
    print('Start @ ' + str( datetime.datetime.now() ) )
    jsonToMySQL(host, user, passwd, db_name, table_name)
    print('Done @ ' + str( datetime.datetime.now() ) )

schedule.every(6).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
