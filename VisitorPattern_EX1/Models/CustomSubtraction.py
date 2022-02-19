from InterpreterPattern_EX1.Models.CustomOperation import CustomOperation


class CustomSubtraction(CustomOperation):
    def __init__(self, left_expression, right_expression):
        self.__left_expression = left_expression
        self.__right_expression = right_expression

    @property
    def left_expression(self):
        return self.__left_expression

    @property
    def right_expression(self):
        return self.__right_expression

    def calculate(self):
        return self.__left_expression.calculate() - self.__right_expression.calculate()

    def accept_visitor(self, visitor):
        visitor.visit_subtraction(self)
