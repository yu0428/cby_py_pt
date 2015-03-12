#!/usr/bin/env python

__author__ = 'chenbingyu'

import cgi
import cgitb
import os
import ViewGenerator
from DBException import UpdateImageError
from DataManager import DataManager


cgitb.enable()  #  for troubleshooting

viewGenerator = ViewGenerator.ViewGenerator()
dataManager = DataManager()

form = cgi.FieldStorage()
fileitem = form['imgfile']

if fileitem.filename:
    #  strip leading path from file name to avoid directory traversal attacks
    #  fn = os.path.basename(fileitem.filename)
    #  open('files/' + fn, 'wb').write(fileitem.file.read())
    try:
        imagedata = fileitem.file.read()
        dataManager.store_image("test4", imagedata)
        viewGenerator.operate_page("The image: "+fileitem.filename+" was uploaded successfully.")
    except UpdateImageError:
        viewGenerator.error_page("An error occurred.Sorry for that.")
else:
    viewGenerator.uploadImage("No file was uploaded.")