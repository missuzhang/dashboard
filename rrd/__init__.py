#-*- coding:utf-8 -*-
import os
from flask import Flask, request, g, session, make_response, redirect
from rrd.api import uic
import logging
#-- create app --
app = Flask(__name__)
app.config.from_object("rrd.config")

IGNORE_PREFIX = ['/api', '/static']
# config log
log_formatter = '%(asctime)s\t[%(filename)s:%(lineno)d] [%(levelname)s: %(message)s]'
log_level = logging.DEBUG if app.config['DEBUG'] else logging.WARNING
logging.basicConfig(format=log_formatter, datefmt="%Y-%m-%d %H:%M:%S", level=log_level)

@app.errorhandler(Exception)
def all_exception_handler(error):
    print "exception: %s" %error
    return u'dashboard 暂时无法访问，请联系管理员', 500


@app.before_request
def before_request():
    p = request.path
    for ignore_pre in IGNORE_PREFIX:
        if p.startswith(ignore_pre):
            return
    
    if 'user_name' in session and session['user_name']:
        g.user_name = session['user_name']
    else:
        sig = request.cookies.get('sig')
        if not sig:
            return redirect_to_sso()

        username = uic.username_from_sso(sig)
        if not username:
            return redirect_to_sso()

        session['user_name'] = username
        g.user_name = session['user_name']

	
def redirect_to_sso():
    logging.debug('sso')
    sig = uic.gen_sig()
    resp = make_response(redirect(uic.login_url(sig, urllib.quote(request.url))))
    resp.set_cookie('sig', sig)
    return resp

from view import api, chart, screen, index
