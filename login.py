#!/usr/bin/env python

__author__ = 'chenbingyu'

# Handle user's "log in" operation:make sure
#  the user name exists and the password is correct.

import DataManager
import ViewGenerator
import cgitb
import cgi

cgitb.enable()  # for troubleshooting.

#  Get user name and password.
form = cgi.FieldStorage()
username = form.getfirst("name", "")
password = form.getfirst("password", "")

dataManager = DataManager.DataManager()
viewGenerator = ViewGenerator.ViewGenerator()

#  Check user's name and password.
if dataManager.namepass_correct(username, password):
    viewGenerator.operate_page()
else:
    viewGenerator.login_page("Name or password is not correct! Try again or register.")