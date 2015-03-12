#!/usr/bin/env python

__author__ = 'chenbingyu'

import Cookie
import os


class SessionManager:
    # Manage user's "log in" or "log out" actions.
    def __init__(self):
        pass

    def login(self, name, first_pass, second_pass):
        pass

    def logout(self, name):
        pass

    def logged(self):

        # Return true if user already logged in.
        cookie = Cookie.SimpleCookie()
        cookie_string = os.environ.get("HTTP_COOKIE")

        if cookie_string:
            return True
        return False