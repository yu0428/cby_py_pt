#!/usr/bin/env python

__author__ = 'chenbingyu'

#  Handle user's "register" operation.

import cgi
import cgitb
import DataManager
import ViewGenerator

cgitb.enable()

form = cgi.FieldStorage()
#  Strip white spaces.
uname = form.getfirst("name", "").strip(' ')
fpass = form.getfirst("first_pass", "").strip(' ')
spass = form.getfirst("second_pass", "").strip(' ')


def process(username, first_pass, second_pass):

    data_manager = DataManager.DataManager()
    view_generator = ViewGenerator.ViewGenerator()

    if "" == username:
        view_generator.register_page("name cannot be empty.")
        return
    if "" == first_pass:
        view_generator.register_page("The first password cannot be empty")
        return
    if "" == second_pass:
        view_generator.register_page("The second password cannot be empty")
        return

    if data_manager.name_not_exist(username):  # username is not used by others.
        if first_pass == second_pass:
            if data_manager.add(username, first_pass):
                view_generator.error_page("Error happened.Sorry for that.Try again later.")
                return
            view_generator.operate_page()
        else:
            view_generator.register_page("passwords are not the same.")
    else:
        view_generator.register_page("name"+username+" is already used.<br>")

process(uname, fpass, spass)