#!/usr/bin/env python

__author__ = 'chenbingyu'

#  Welcome page.

import cgitb

from Session.SessionManager import SessionManager
from ViewGenerator import ViewGenerator


cgitb.enable()  # for troubleshooting

sessionManager = SessionManager()
viewGenerator = ViewGenerator()

user = sessionManager.logged()
if user:
    #  Generate an operate page for logged users.
    viewGenerator.operate_page("Welcome "+user)
else:
    # Generate a welcome page for new users.
    viewGenerator.welcome_page()