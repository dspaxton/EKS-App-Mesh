#!/usr/bin/env python3
import os, os.path
import urllib.request
from urllib.parse import urlparse
import cherrypy
import json
import requests
import pdb

# catalog = os.environ['CATALOG']
# access_key = os.environ['AWS_ACCESS_KEY_ID']
# secret_key = os.environ['AWS_SECRET_ACCESS_KEY']
# session_token = os.environ['AWS_SESSION_TOKEN']



class frontend(object):
    @cherrypy.expose
    def index(self):
        # response = urllib.request.urlopen('http://db.private-example.com:8080/')
        # output = response.read().decode('utf-8')
        dburl = "http://db.private-example.com:8080/"
        dboutput = requests.get(dburl)
        html = """<html>
        <title>Frontend</title>
        <center>
          <head>
            <link href="/static/css/style.css" rel="stylesheet">
          </head>
          <h1>FrontEnd</h1>
          <body>
          <p>Welcome to the V3 frontend running on ECS Fargate
          <p>
          """
        #html += str(backendoutput) + "<BR>"
        html += "Latest stock info:" + str(dboutput.text)
        html += """</head>
          </html>
          """
        return html



    @cherrypy.expose
    def ping(self):
        return "OK"


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            # 'tools.response_headers.headers': [('Content-Type', 'text/plain')],
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    #cherrypy.quickstart(tradechecker(), '/', conf)
    cherrypy.config.update({'server.socket_host':'127.0.0.1','server.socket_port':8080})
    cherrypy.quickstart(frontend(), '/', conf)
