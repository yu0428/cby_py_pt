#!/usr/bin/env python

__author__ = 'chenbingyu'

# Handle user's "register" operation.

import cgi
import cgitb

from DataModel.DataManager import DataManager
from ViewGenerator import ViewGenerator
from Session.SessionManager import SessionManager
from DataModel.DBException import DuplicateKeyError


cgitb.enable()

form = cgi.FieldStorage()
#  Strip white spaces.
uname = form.getfirst("name", "").strip(' ')
fpass = form.getfirst("first_pass", "").strip(' ')
spass = form.getfirst("second_pass", "").strip(' ')


def process(username, first_pass, second_pass):
    data_manager = DataManager()
    view_generator = ViewGenerator()

    if "" == username:
        view_generator.register_page("name cannot be empty.")
        return

    if "" == first_pass:
        view_generator.register_page("The first password cannot be empty")
        return

    if "" == second_pass:
        view_generator.register_page("The second password cannot be empty")
        return

    if first_pass == second_pass:
        try:
            data_manager.add(username, first_pass)
            #  Start session
            session = SessionManager()
            session_info = session.start_session(username)

            #  Registration is successful.
            view_generator.operate_page("Welcome " + username, session_info)  # Jump to the "operate" page.
        except DuplicateKeyError as dke:
            view_generator.register_page(dke.error)
            return
        except Exception:
            view_generator.error_page("Some strange error occurred.Sorry for that")
            return
    else:
        view_generator.register_page("passwords are not the same.")


process(uname, fpass, spass)