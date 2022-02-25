# import MySQLdb

class ConnectionFactory:

    @staticmethod
    def get_connection():
        return MySQLdb.connect(
            host='localhost',
            user='root',
            password='',
            db='DatabaseName')


# Just to avoid installing the actual package
class MySQLdb:
    pass

