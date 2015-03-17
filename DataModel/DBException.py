__author__ = 'chenbingyu'

#  QueryDbError stands for database query errors.


class QueryDbError:
    def __init__(self, error=""):
        self.error = error

#  DuplicateKeyError means "Duplicate key" error from
#  database insert operation.


class DuplicateKeyError:
    def __init__(self, error):
        self.error = error


#  UpdateImageError stands for errors occurring when
#  the users are uploading images.


class UpdateImageError:
    def __init__(self, error):
        self.error = error

#  ReadImageError stands for errors occurring when reading images.


class ReadImageError:
    def __init__(self, error):
        self.error = error