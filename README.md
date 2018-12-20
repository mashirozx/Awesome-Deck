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
Cards data from [HearthstoneJSON](https://github.com/HearthSim/hsdata), this script will get the latest Json data automatically. 

Initialize the Database with:
```shell
python db_initial.py
```

<details>
<summary>Auto Start Configuration</summary>

Latter if you need a cards data auto update (who knows when Bilzzard will release a hotfix and diminish some cards), there's a auto update database script `auto_update.py`, add it to system autostart task, and then for every 6 hours (you may change is to any interval by modifying the scrpit).

On a Ubuntu 18+, you may do so:

Create unit file in `/lib/systemd/system/hearthstone_deck_auto_update.service` with the following content:

```
[Unit]
Description=<hearthstone_deck_auto_update>
After=network.target network-online.target

[Service]
Type=simple
User=<required_user_name>
Group=<required_group_name>
Restart=always
ExecStartPre=/bin/mkdir -p /var/run/<hearthstone_deck_auto_update>
PIDFile=/var/run/<hearthstone_deck_auto_update>/service.pid
ExecStart=/path/to/your/auto_update.py

[Install]
WantedBy=multi-user.target
```
Save this file and reload systemd:

```shell
sudo systemctl daemon-reload
```

Then add your service to autostart:

```
sudo systemctl enable hearthstone_deck_auto_update.service
```

you should see that Systemd created required symlinks after enable action.

Reboot and see if it's up and running (ps aux | grep python or sudo systemctl status hearthstone_deck_auto_update.service). If there is something weird - check Systemd journal:

```
sudo journalctl -xe
```
</details>

### Run web service

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
