#!/usr/bin/env python

__author__ = 'chenbingyu'

# This script is the API,which anyone can use to
#  get an Image of an specific user.For example,
#  url:/cgi-bin/getimage.py?u=user1,will send back a
#  response containing  the image of user "user1".
#  If there is no image for "user1",a default image will be sent back.
#  If "user1" don't exist,an "error" image will be sent

import cgi
import cgitb

from DataModel.DataManager import DataManager
from ViewGenerator import ViewGenerator


cgitb.enable()

dataManager = DataManager()
viewGenerator = ViewGenerator()

query_parameters = cgi.FieldStorage()
#  Get the "target_page" parameter.
target_user = query_parameters.getfirst("u", "")

imagedata = None

if "" == target_user or not dataManager.user_exist(target_user):
    imagedata = dataManager.error_image()
else:
    imagedata = dataManager.read_image(target_user)

viewGenerator.checkimage_page(imagedata)