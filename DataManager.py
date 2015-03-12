#!/usr/bin/env python

__author__ = 'chenbingyu'

#  Class DataManager is responsible for handing
#  users' data including user name,password.
#  DataManager also takes care of users' session
#  information because they are all stored in the
#  same database.

import mysql
import dbconfparser
from mysql.connector import MySQLConnection, Error
from DBException import DuplicateKeyError
from DBException import QueryDbError
from DBException import UpdateImageError
from DBException import ReadImageError


class DataManager:
    def __init__(self):
        self.hashkey = "hash,123"
        self.dbconf = dbconfparser.read_db_config()

    def namepass_correct(self, name="", password=""):
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
        except Error as e:
                raise QueryDbError(e.message)
        finally:
            cursor.close()
            conn.close()
        return result

    def add(self, username="", password=""):
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
        query = "SELECT image FROM user WHERE username = %s"
        try:
            # query blob data form the "user" table
            conn = MySQLConnection(**self.dbconf)
            cursor = conn.cursor()
            cursor.execute(query, (username,))
            image = cursor.fetchone()[0]
            return image
        except Error as e:
            raise ReadImageError(e.message)
        finally:
            cursor.close()
            conn.close()
