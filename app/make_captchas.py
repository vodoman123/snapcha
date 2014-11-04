import os
import random

import sys
sys.path.insert(0, 'libs')

from Captcha.Visual.Tests import PseudoGimpy

root_folder = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
images_folder = os.path.join(root_folder,'static/images/captchas/')

print random.choice(random.choice(os.listdir('static/images/captchas')))	