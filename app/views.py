from flask import Flask, render_template, request, redirect, url_for
from app import app
import os
import random

import boto
from boto.s3.key import Key
from boto.s3.connection import S3Connection


import sys
sys.path.insert(1, 'app/libs')

from snapchat import Snapchat

s = Snapchat()
s.login('', '')

conn = S3Connection('', '')
snapchat_captcha = conn.get_bucket('')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/snapcha', methods=['GET'])
def snapcha():
	snap_name = request.args['snap-name']

	root_folder = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
	images_folder = os.path.join(root_folder,'static/images/captchas/')
	choose_captcha = str(random.choice(os.listdir(images_folder)))
	
	media_id = s.upload(Snapchat.MEDIA_IMAGE, os.path.join(images_folder,choose_captcha))
	#media_id = s.upload(Snapchat.MEDIA_IMAGE, snapchat_captcha.get_key('').get_contents_as_string())
	s.send(media_id, snap_name)
	
	return redirect(url_for('result'))

@app.route('/result', methods=['GET'])
def result():
	return "hello"
