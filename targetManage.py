#!/usr/bin/env python

__author__ = 'chenbingyu'

# Generate the corresponding page according to the "target_page"
#  parameter in the query string.
#  For example,the url,/cgi-bin/targetManage.py?target_page=login,
#  will make targetManage.py generate a login page.

import cgi
import cgitb

from ViewGenerator import ViewGenerator
from Session.SessionManager import SessionManager
from DataModel.DataManager import DataManager


cgitb.enable()  # for troubleshooting

viewGenerator = ViewGenerator()

query_parameters = cgi.FieldStorage()
#  Get the "target_page" parameter.
target_page = query_parameters.getfirst("target_page", "")

if "login" == target_page:
    #  Generate a "login" page
    viewGenerator.login_page()

elif "logout" == target_page:
    #  End the session:delete cookie information from the browsers.
    session = SessionManager()
    session_info = session.end_session()

    # Jump to welcome page.
    viewGenerator.welcome_page(session_info)

elif "register" == target_page:
    viewGenerator.register_page()

elif "upload_image" == target_page:
    viewGenerator.uploadimage_page()

elif "check_image" == target_page:
    dataManager = DataManager()

    session = SessionManager()
    name = session.logged()
    if name:  # The user has logged in.
        imagedata = dataManager.read_image(name)
        viewGenerator.checkimage_page(imagedata)
    else:  # The user needs to log in.
        viewGenerator.welcome_page()
else:
    viewGenerator.no_page()
