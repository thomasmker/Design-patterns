from StatePattern_EX1.Models.BudgetState import InProgress


class Budget(object):

    def __init__(self, value):
        self.__value = value
        self.current_state = InProgress()
        self.__extra_discount = 0

    @property
    def value(self):
        return self.__value - self.__extra_discount

    def apply_extra_discount(self):
        self.current_state.apply_extra_discount(self)

    def add_extra_discount(self, discount):
        self.__extra_discount += discount

    def approve(self):
        self.current_state.approve(self)

    def deny(self):
        self.current_state.deny(self)

    def close(self):
        self.current_state.close(self)

