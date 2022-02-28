from Interpreter.EXAMPLE_1.Models.CustomOperation import CustomOperation


class CustomSum(CustomOperation):
    def __init__(self, left_expression, right_expression):
        self.__left_expression = left_expression
        self.__right_expression = right_expression

    def calculate(self):
        return self.__left_expression.calculate() + self.__right_expression.calculate()
