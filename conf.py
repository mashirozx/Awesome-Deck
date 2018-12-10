import configparser

config = configparser.ConfigParser()
#config.sections()
config.read('conf.ini')
#config.sections()
config['DATABASE']['HearthstoneVersion']

db_conf = config['DATABASE']

host = db_conf['Host']
user = db_conf['User']
passwd = db_conf['Password']
db_name = db_conf['Database']
table_name = db_conf['TablePrefix'] + db_conf['HearthstoneVersion']
