#!/usr/bin/env python

__author__ = 'chenbingyu'

#  Generate the corresponding page according to the "target_page"
#  parameter in the query string.
#  For example,the url,/cgi-bin/ViewManage.py?target_page=login,
#  will make ViewManage.py generate a login page.

import cgi
import cgitb
import ViewGenerator

cgitb.enable()  # for troubleshooting

viewGenerator = ViewGenerator.ViewGenerator()

query_parameters = cgi.FieldStorage()
#  Get the "target_page" parameter.
target_page = query_parameters.getfirst("target_page", "")

if "login" == target_page:
    #  Generate a "login" page
    viewGenerator.login_page()

elif "logout" == target_page:
    #  To do:Delete user's session information.
    viewGenerator.welcome_page()

elif "register" == target_page:
    viewGenerator.register_page()

elif "upload_image" == target_page:
    viewGenerator.uploadImage()

elif "check_image" == target_page:
    viewGenerator.checkImage()

else:
    viewGenerator.no_page()
