#-*-coding:utf8-*-
import os


# -- cookie config --
SECRET_KEY = "4e.5tyg8-u9ioj"
SESSION_COOKIE_NAME = "falcon-dashbord"
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30
#--uic config--
UIC_ADDRESS = {
    'internal': 'http://127.0.0.1:1234',
    'external': 'http://192.168.136.131:1234',
}

UIC_TOKEN = ''
#-- dashboard db config --
DASHBOARD_DB_HOST = "127.0.0.1"
DASHBOARD_DB_PORT = 3306
DASHBOARD_DB_USER = "root"
DASHBOARD_DB_PASSWD = ""
DASHBOARD_DB_NAME = "dashboard"

#-- graph db config --
GRAPH_DB_HOST = "127.0.0.1"
GRAPH_DB_PORT = 3306
GRAPH_DB_USER = "root"
GRAPH_DB_PASSWD = ""
GRAPH_DB_NAME = "graph"

#-- app config --
DEBUG = True
SECRET_KEY = "secret-key"
SESSION_COOKIE_NAME = "falcon_dashbord"
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30
SITE_COOKIE = "open-falcon-ck"

#-- query config --
QUERY_ADDR = "http://127.0.0.1:9966"

BASE_DIR = "/root/work/github.com/open-falcon/dashboard/"
LOG_PATH = os.path.join(BASE_DIR,"log/")

try:
    from rrd.local_config import *
except:
    pass
