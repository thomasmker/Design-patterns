from MementoPattern_EX1.Models.ContractState import ContractState


class Contract(object):
    def __init__(self, contract_date, client, contract_type = "NEW"):
        self.__contract_date = contract_date
        self.__client = client
        self.__contract_type = contract_type

    @property
    def contract_date(self):
        return self.__contract_date

    @contract_date.setter
    def date(self, contract_date):
        self.__contract_date = contract_date

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, client):
        self.__client = client

    @property
    def contract_type(self):
        return self.__contract_type

    @contract_type.setter
    def contract_type(self, contract_type):
        self.__contract_type = contract_type

    def next(self):
        if self.__contract_type == 'NEW':
            self.__contract_type = 'IN PROGRESS'
        elif self.__contract_type == 'IN PROGRESS':
            self.__contract_type = 'APPROVED'
        elif self.__contract_type == 'APPROVED':
            self.__contract_type = 'CLOSED'

    def save_state(self):
        return ContractState(Contract(contract_date=self.__contract_date,
                                      client=self.__client,
                                      contract_type=self.__contract_type))

    def restore_state(self, contract_state):
        self.__contract_date = contract_state.contract.contract_date
        self.__client = contract_state.contract.client
        self.__contract_type = contract_state.contract.contract_type

    def __str__(self):
        return f'Date: {self.__contract_date} Client:{self.__client} Type:{self.__contract_type}'
