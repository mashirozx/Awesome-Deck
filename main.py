from json_to_mysql.json_to_mysql import *

host='localhost'
user='root'
passwd='password'
db='hearthstone'
table_name='cards_data_27845'
json_file='json_to_mysql/cards.json'

jsonToMySQL(host, user, passwd, db, table_name, json_file)

key = input('Press any key to quit')
quit()
