import boto
from boto.s3.key import Key
from boto.s3.connection import S3Connection

from PIL import Image

conn = S3Connection('AKIAIP5X6OBUBDHP6CXA', 'pBPDQlNcPeAr3vEAC8LZKEXgR0TGR9PLpNeSvxR8')
snapcha = conn.get_bucket('snapcha')

captcha = snapcha.get_key('captchas/addition.jpg')


key.get_file(file)
Image.open(file)

