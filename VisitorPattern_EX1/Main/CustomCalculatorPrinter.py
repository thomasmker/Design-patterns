
from VisitorPattern_EX1.Models.CustomSum import CustomSum
from VisitorPattern_EX1.Models.CustomSubtraction import CustomSubtraction
from VisitorPattern_EX1.Models.CustomNumber import CustomNumber
from VisitorPattern_EX1.Models.Printer import Printer


def main():
    left_expression = CustomSum(CustomNumber(10), CustomNumber(2))
    right_expression = CustomSubtraction(CustomNumber(10), CustomNumber(5))
    final_calculation_expression = CustomSum(left_expression, right_expression)

    visitor = Printer()
    final_calculation_expression.accept_visitor(visitor)


if __name__ == '__main__':
    main()
