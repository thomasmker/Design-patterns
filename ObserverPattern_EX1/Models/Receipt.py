from datetime import date


class Receipt:
    def __init__(self, customer, item, emission_date=date.today(), details='', observers=[]):
        if len(details) > 20:
            raise Exception('Details must not exceed 20 characters')
        self.__customer = customer
        self.__item = item
        self.__emission_date = emission_date
        self.__details = details
        self.__observers = observers

    @property
    def customer(self):
        return self.__customer

    @property
    def item(self):
        return self.__item

    @property
    def emission_date(self):
        return self.__emission_date

    @property
    def details(self):
        return self.__details

    def notify_observers(self):
        for observer in self.__observers:
            observer(self)

    def __str__(self):
        return f'Customer:{self.__customer} ' \
               f'Item:{self.__item} ' \
               f'Emission date:{self.__emission_date} ' \
               f'Details:{self.__details}'
