#!/usr/bin/env python

__author__ = 'chenbingyu'

#  Welcome page.

import cgitb
import SessionManager
import ViewGenerator

cgitb.enable()  # for troubleshooting

sessionManager = SessionManager.SessionManager()
viewGenerator = ViewGenerator.ViewGenerator()

if sessionManager.logged():
    #  Generate an operate page for logged users.
    viewGenerator.operate_page()
else:
    # Generate a welcome page for new users.
    viewGenerator.welcome_page()