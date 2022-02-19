class ContractState:
    def __init__(self, contract):
        self.__contract = contract

    @property
    def contract(self):
        return self.__contract
