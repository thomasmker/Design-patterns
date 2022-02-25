# import MySQLdb
from Factory.EXAMPLE_1.Models.ConnectionFactory import ConnectionFactory


def main():
    connection = ConnectionFactory.get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM cursor')
    for line in cursor:
        print(line)

    connection.close()


if __name__ == '__main__':
    main()
