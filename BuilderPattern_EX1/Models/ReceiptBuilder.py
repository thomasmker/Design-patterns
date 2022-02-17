from datetime import date
from BuilderPattern_EX1.Models.Receipt import Receipt


class ReceiptBuilder:
    def __init__(self):
        self.__customer = None
        self.__item = None
        self.__emission_date = None
        self.__details = None

    def with_customer(self, customer):
        self.__customer = customer
        return self

    def with_item(self, item):
        self.__item = item
        return self

    def with_emission_date(self, emission_date):
        self.__emission_date = emission_date
        return self

    def with_details(self, details):
        self.__details = details
        return self

    def build(self):
        self.__init_and_validate()

        return Receipt(
            customer=self.__customer,
            item=self.__item,
            emission_date=self.__emission_date,
            details=self.__details
        )

    def __init_and_validate(self):
        if self.__customer is None:
            raise Exception('Customer must be provided')
        if self.__item is None:
            raise Exception('Item must be provided')
        if self.__emission_date is None:
            self.__emission_date = date.today()
        if self.__details is None:
            self.__details = ''

