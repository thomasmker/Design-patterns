from InterpreterPattern.EXAMPLE_1.Models.CustomSum import CustomSum
from InterpreterPattern.EXAMPLE_1.Models.CustomSubtraction import CustomSubtraction
from InterpreterPattern.EXAMPLE_1.Models.CustomNumber import CustomNumber


def main():
    left_expression = CustomSubtraction(CustomNumber(10), CustomNumber(5))
    right_expression = CustomSum(CustomNumber(2), CustomNumber(10))
    final_calculation_expression = CustomSum(left_expression, right_expression)

    result = final_calculation_expression.calculate()
    print(result)


if __name__ == '__main__':
    main()
