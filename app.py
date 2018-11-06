#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle
from bottle import run, route, static_file, error, request, default_app, get, response, template, redirect
import datetime
import html

import os
from os import environ as env
from sys import argv

@route("/")
def index():
    nyar_vorur = []
    if request.get_cookie("ny-vara") != None:
        nyar_vorur = list(request.get_cookie("ny-vara"))
    return template('index', nyvor=nyar_vorur)

@route('/static/<skra:path>')
def static_skrar(skra):
    return static_file(skra, root='./public/')

@route('/vorur')
def sida2():
    voru_num = request.query.vara
    ts = datetime.datetime.now() + datetime.timedelta(days=365)
    response.set_cookie("ny-vara", voru_num, expires=ts)
    if request.get_cookie("ny-vara") != None:
        if len(request.get_cookie("ny-vara")) < 3:
            response.set_cookie("ny-vara", voru_num + request.get_cookie("ny-vara"), expires=ts)
        else:
            response.set_cookie("ny-vara", voru_num + request.get_cookie("ny-vara")[:-1], expires=ts)

    return template('vara', num=voru_num)

bottle.run(host='0.0.0.0', port=argv[1])
