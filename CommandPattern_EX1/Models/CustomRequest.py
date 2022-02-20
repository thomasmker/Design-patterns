from datetime import date


class CustomRequest:
    def __init__(self, client, value):
        self.__client = client
        self.__value = value
        self.__status = 'NEW'
        self.__conclusion_date = None

    @property
    def client(self):
        return self.__client

    @property
    def value(self):
        return self.__value

    @property
    def status(self):
        return self.__status

    @property
    def conclusion_date(self):
        return self.__conclusion_date

    def pay(self):
        self.__status = 'PAID'

    def conclude(self):
        self.__conclusion_date = date.today()
        self.__status = 'CONCLUDED'

    def __str__(self):
        return f'Client:{self.__client} Status:{self.__status} Conclusion date: {self.__conclusion_date}'
