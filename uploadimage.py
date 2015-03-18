#!/usr/bin/env python

__author__ = 'chenbingyu'

import cgi
import cgitb

from ViewGenerator import ViewGenerator
from Session.SessionManager import SessionManager
from DataModel.DBException import UpdateImageError
from DataModel.DataManager import DataManager


cgitb.enable()  # for troubleshooting

viewGenerator = ViewGenerator()
dataManager = DataManager()

form = cgi.FieldStorage()
fileitem = form['imgfile']

if fileitem.filename:
    # strip leading path from file name to avoid directory traversal attacks
    # fn = os.path.basename(fileitem.filename)
    #  open('files/' + fn, 'wb').write(fileitem.file.read())
    try:
        imagedata = fileitem.file.read()

        if len(imagedata) > 5242880:
            viewGenerator.operate_page("The image is too large."
                                       "It should be less than 5MB")
        else:
            session = SessionManager()
            name = session.logged()

            if name:  # User has logged in.
                dataManager.store_image(name, imagedata)
                viewGenerator.operate_page("The image: " + fileitem.filename +
                                           " was uploaded successfully.")
            else:
                viewGenerator.welcome_page()
    except UpdateImageError as ue:
        viewGenerator.error_page("An error occurred.Sorry for that.")
else:
    viewGenerator.uploadimage_page("No file was uploaded.")