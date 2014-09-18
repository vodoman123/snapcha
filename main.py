#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urllib
import urllib2
import jinja2
import os

import sys
sys.path.insert(0, 'libs')

import requests

from google.appengine.api import urlfetch
from snapchat import Snapchat
from Captcha.Visual.Tests import PseduoGimpy

s = Snapchat()
s.login('', '')

g = PseudoGimpy()

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(main_template.render())

class YoOauth(webapp2.RequestHandler):
    def get(self):
        yo_name = self.request.get('yo-name')
        fctn = SnapFunc()
        yo_user = fctn.send_snapcha(yo_name)
        yoauth_template = JINJA_ENVIRONMENT.get_template('templates/yoauth.html')
        self.response.write(yoauth_template.render())

class SnapFunc:
	def send_snapcha(userName):
		i = g.render()
		i.save("output.jpg")

		media_id = s.upload(Snapchat.MEDIA_IMAGE, 'output.jpg')
		s.send(media_id, userName)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/yoauth', YoOauth)
], debug=True)
