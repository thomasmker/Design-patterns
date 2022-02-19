class ContractHistory:
    def __init__(self):
        self.__saved_states = []

    def get_state(self, index):
        return self.__saved_states[index]

    def add_state(self, contract_state):
        self.__saved_states.append(contract_state)

