# Hearthstone Deck Embed Tool

A simple Hearthstone card deck API that you can easily embed in your site with iframe. The backend of [Awesome Deck](https://deck.2heng.xin/).

Work with Python3, Django, and MySQL/MariaDB.

## How to Use

### Requirements
Install pip for Python3:
```shell
apt install python3-pip
```

Install required packages:
```shell
pip install -r requirements.txt
```

If you see something like:
> EnvironmentError: mysql_config not found

You should install libmysqlclient-dev:
```shell
sudo apt install default-libmysqlclient-dev
```

### Configuration
Rename the configuration file `conf.sample.ini` as `conf.ini`, and fill in your info.

### Initialize Database
Cards data from [HearthstoneJSON](https://github.com/HearthSim/hsdata), get the latest Json data [here](https://api.hearthstonejson.com/v1/).

Initialize the Database with:
```shell
python db_initial.py
```

Then you can run the test server:
```shell
python web/manage.py runserver 0.0.0.0:8000
```

Or run with uwsgi:
```shell
cd web/web
uwsgi --http :8000 --module web.wsgi
```

Then visit: <http://127.0.0.1:8000/>.

### Author
© [Mashiro](https://github.com/mashirozx/), Released under the [MIT](https://github.com/mashirozx/hearthstone-deck-embed/blob/master/LICENSE) License.
