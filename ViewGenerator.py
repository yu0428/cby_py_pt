#!/usr/bin/env python

__author__ = 'chenbingyu'


class ViewGenerator:  # Response for generating user interface files(html file).
    def __init__(self):
        #  login,register,logout,upload image,check image
        self.htmlFile = """
            <!DOCTYPE html>
            <html>
                <head lang="en">
                    <meta charset="UTF-8">
                    <title>Welcome</title>
                </head>
                <body>
                    %s
                    %s
                    %s
                </body>
            </html>
        """
        self.login = """
            <a href="/cgi-bin/targetManage.py?target_page=login">Login</a>
            """
        self.register = """
            <a href="/cgi-bin/targetManage.py?target_page=register">Register</a>
            """
        self.uploadImage = """
            <a href="/cgi-bin/targetManage.py?target_page=upload_image">Upload Image</a>
            """
        self.checkImage = """
            <a href="/cgi-bin/targetManage.py?target_page=check_image">Check Image</a>
            """
        self.logout = """
            <a href="/cgi-bin/targetManage.py?target_page=logout">Logout</a>
            """

    def welcome_page(self):
        #  Generate a html page containing "Login" or "Register" links.
        print("Content-Type: text/html\n")
        print(self.htmlFile % (self.login, self.register, ""))

    def operate_page(self):
        # Generate a html page containing "Logout","Upload Image" or "Check Image" links.
        print("Content-Type: text/html\n")
        print(self.htmlFile % (self.logout, self.uploadImage, self.checkImage))

    def login_page(self, message=""):
        # Generate a "Login"
        login_form = """
            <form method="post" action="/cgi-bin/login.py">
                Name: <input type="text" name="name">
                <br>
                Password:<input type="password" name="password">
                <br>
                <input type="submit" value="Submit">
                <input type="reset" value="Reset">
            </form>
        """
        print("Content-Type: text/html\n")
        print(self.htmlFile % (login_form, message, ""))

    def register_page(self):
        #  Generate a "Register page"
        register_form = """
            <form method="post" action="/cgi-bin/register.py">
                Name: <input type="text" name="name">
                <br>
                Password:<input type="password" name="pass_first">
                <br>
                Password again:<input type="password" name="pass_second">
                <br>
                <input type="submit" value="Submit">
                <input type="reset" value="Reset">
            </form>
        """
        print("Content-Type: text/html\n")
        print(self.htmlFile % (register_form, "", ""))

    def no_page(self):
        print("Content-Type: text/html\n")
        print(self.htmlFile % ("The page you requested doesn't exist!", "", ""))

    def error_page(self, error=""):
        print("Content-Type: text/html\n")
        print(self.htmlFile % (error, "", ""))