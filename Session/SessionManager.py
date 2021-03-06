#!/usr/bin/env python

__author__ = 'chenbingyu'

import Cookie
import os


class SessionManager:
    # Manage user's "log in" or "log out" actions.
    def __init__(self):
        pass

    @staticmethod
    def start_session(name):
        cookie_message = 'Set-Cookie: u=' + name
        return cookie_message

    @staticmethod
    def end_session():
        cookie_meesage = "Set-Cookie: u=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT;"
        return cookie_meesage

    @staticmethod
    def logged():
        # Return user name if user already logged in.
        # Otherwise,None will be returned.
        cookie = Cookie.SimpleCookie()
        cookie_string = os.environ.get("HTTP_COOKIE")

        if cookie_string:
            cookie.load(cookie_string)
            #  return user name.
            username = cookie['u'].value

            if username != "deleted":
                return username