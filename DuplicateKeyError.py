#!/usr/bin/env python

__author__ = 'chenbingyu'

#  DuplicateKeyError means "Duplicate key" error from
#  database insert operation.

class DuplicateKeyError:
    def __init__(self, error):
        self.error = error
