#!/usr/bin/env python

__author__ = 'chenbingyu'

import Cookie
import os

class SessionManager:
    # Manage user's "log in" or "log out" actions.
    def __init__(self):
        pass

    def start_session(self, name):
        cookie_message = 'Set-Cookie: u=' + name
        return cookie_message

    def end_session(self):
        cookie_meesage="Set-Cookie: reg_fb_gate=deleted; Expires=Thu, 01-Jan-1970 00:00:01 GMT;"
        return cookie_meesage

    def logged(self):
        #  Return user name if user already logged in.
        #  Otherwise,None will be returned.
        cookie = Cookie.SimpleCookie()
        cookie_string = os.environ.get("HTTP_COOKIE")

        if cookie_string:
            return cookie['u'].value