from StrategyPattern_EX1.budget import Budget
from StrategyPattern_EX1.taxes import FederalTax, MunicipalTax
from StrategyPattern_EX1.taxes_calculator import TaxesCalculator


def main():
    calculator = TaxesCalculator()
    budget = Budget(100)
    calculator.calculate(budget, FederalTax())
    calculator.calculate(budget, MunicipalTax())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

