#!/usr/bin/env python

__author__ = 'chenbingyu'

#  Class DataManager is responsible for handing
#  users' data including user name,password.
#  DataManager also takes care of users' session
#  information because they are all stored in the
#  same database.

from mysql.connector import MySQLConnection, Error

from DataModel import dbconfparser
from DataModel.DBException import DuplicateKeyError
from DataModel.DBException import QueryDbError
from DataModel.DBException import UpdateImageError
from DataModel.DBException import ReadImageError


class DataManager:
    def __init__(self):
        self.hashkey = "hash,123"
        self.dbconf = dbconfparser.read_db_config()

    def namepass_correct(self, name="", password=""):
        #  True:name and password are both correct.
        #  False:one of them are not correct.

        query = "select name from user where name=%s and password = password(%s)"
        args = (name, password+self.hashkey)
        result = False
        try:
            conn = MySQLConnection(**self.dbconf)
            cursor = conn.cursor()
            cursor.execute(query, args)

            row = cursor.fetchone()

            if row is not None:
                result = True
            return result
        except Error as e:
                raise QueryDbError(e.message)
        finally:
            cursor.close()
            conn.close()

    def add(self, username="", password=""):
        #  "deleted" will be used by SessionManager to
        #  delete cookie from user browsers.
        #  This is not a good solution. A better on
        #  will be used in the future.
        if username == "deleted":
            raise DuplicateKeyError("name:"+username+" is already used.")

        #  register a new user with "username" and "password".
        query = "insert user(name,password) values(%s,password(%s))"
        args = (username, password+self.hashkey)

        try:
            conn = MySQLConnection(**self.dbconf)
            cursor = conn.cursor()
            cursor.execute(query, args)

            conn.commit()
        except Error as error:
            if 1062 == error.errno:  # This is mysql specific.
                raise DuplicateKeyError("name:"+username+" is already used.")
            else:
                raise Exception(error.message)
        finally:
            cursor.close()
            conn.close()

    def store_image(self, name, imagedata):

        # prepare update query and data
        query = "update user " \
                "set image = %s " \
                "where name  = %s"
        args = (imagedata, name)
        try:
            conn = MySQLConnection(**self.dbconf)
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
        except Error as e:
            raise UpdateImageError(e.message)
        finally:
            cursor.close()
            conn.close()

    def read_image(self, username):
        # select image column of a specific user.
        query = "SELECT image FROM user WHERE name = %s"
        try:
            # query blob data form the "user" table
            conn = MySQLConnection(**self.dbconf)
            cursor = conn.cursor()
            cursor.execute(query, (username,))
            image = cursor.fetchone()
            if image and image[0]:
                return image[0]

            #  Read default image.
            f = open("./images/default.jpeg", 'rb')
            return f.read()
        except Error as e:
            raise ReadImageError(e.message)
        finally:
            cursor.close()
            conn.close()

    def error_image(self):
        f = open("./images/error.jpeg", "rb")
        return f.read()

    def user_exist(self, username):
        #  If "username" exists,True will be returned.
        #  Otherwise False.
        query = "SELECT name FROM user WHERE name = %s"
        try:
            conn = MySQLConnection(**self.dbconf)
            cursor = conn.cursor()
            cursor.execute(query, (username,))
            u = cursor.fetchone()
            if u:  # Not null.
                return True
            return False
        except Error as e:
            raise QueryDbError(e.message)
        finally:
            cursor.close()
            conn.close()


