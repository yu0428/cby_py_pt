#!/usr/bin/env python

__author__ = 'chenbingyu'

# Handle user's "log in" operation:make sure
# the user name exists and the password is correct.

import cgitb
import cgi

from DataModel.DataManager import DataManager
from ViewGenerator import ViewGenerator
from Session.SessionManager import SessionManager
from DataModel.DBException import QueryDbError


cgitb.enable()  # for troubleshooting.

#  Get user name and password.
form = cgi.FieldStorage()
username = form.getfirst("name", "").strip(' ')
password = form.getfirst("password", "").strip(' ')

dataManager = DataManager()
viewGenerator = ViewGenerator()


def check_name_password(name="", pw=""):
    if "" == name or "" == pw:
        viewGenerator.login_page("name or password is not correct.")
        return

    #  Check user's name and password.
    try:
        res = dataManager.namepass_correct(username, password)
        if res:
            #  Start a session.
            session = SessionManager()
            session_info = session.start_session(username)

            viewGenerator.operate_page("Welcome " + username, session_info)
        else:
            viewGenerator.login_page("name or password is not correct.")
    except QueryDbError:
        viewGenerator.error_page("An error happened.Sorry for that.")


check_name_password(username, password)