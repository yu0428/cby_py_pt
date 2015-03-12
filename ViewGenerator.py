#!/usr/bin/env python

__author__ = 'chenbingyu'

#  Class ViewGenerator responsible for generating "login","register",
#  "Upload Image","Check Image" and so on pages.

class ViewGenerator:
    # Response for generating user interface files(html file).
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
                    <br/>
                    %s
                    <br/>
                    %s
                    <br/>
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
        print(self.htmlFile % (self.login, self.register, "", ""))

    def operate_page(self, message=""):
        # Generate a html page containing "Logout","Upload Image" or "Check Image" links.
        print("Content-Type: text/html\n")
        print(self.htmlFile % (message, self.logout, self.uploadImage, self.checkImage))

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
        print(self.htmlFile % (login_form, message, "", ""))

    def register_page(self, message=""):
        #  Generate a "Register page"
        register_form = """
            <form method="post" action="/cgi-bin/register.py">
                White spaces at the beginning or in the end will be ignored.
                <br>
                Name: <input type="text" name="name">
                <br>
                Password:<input type="password" name="first_pass">
                <br>
                Password again:<input type="password" name="second_pass">
                <br>
                <input type="submit" value="Submit">
                <input type="reset" value="Reset">
            </form>
        """
        print("Content-Type: text/html\n")
        print(self.htmlFile % (register_form, message, "", ""))

    def uploadImage_page(self, message=""):
        upload_form = """
            <form action="/cgi-bin/uploadimage.py" method="post"
                enctype="multipart/form-data" name="upload_form">
                <label>Upload an image(.jpeg for now).</label>
                <br/>
                <input name="imgfile" type="file" accept="image/jpeg"/>
                <br/>
                <input name="upload" type="submit"/>
                <br/>
                <input name="reset" type="reset"/>
            </form>
        """
        print("Content-Type: text/html\n")
        print(self.htmlFile % (upload_form, message, "", ""))

    def checkImage_page(self):
        pass

    def no_page(self):
        print("Content-Type: text/html\n")
        print(self.htmlFile % ("The page you requested doesn't exist!", "", "", ""))

    def error_page(self, error=""):
        print("Content-Type: text/html\n")
        print(self.htmlFile % (error, "", "", ""))