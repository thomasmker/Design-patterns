from InterpreterPattern_EX1.Models.CustomOperation import CustomOperation


class CustomNumber(CustomOperation):
    def __init__(self, number):
        self.__number = number

    def calculate(self):
        return self.__number
