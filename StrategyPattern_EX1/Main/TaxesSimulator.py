from StrategyPattern_EX1.Models.budget import Budget
from StrategyPattern_EX1.Models.taxes import FederalTax, MunicipalTax
from StrategyPattern_EX1.Models.taxes_calculator import TaxesCalculator


def main():
    calculator = TaxesCalculator()
    budget = Budget(500)
    print('Taxes:')
    print(f'Federal = {calculator.calculate(budget, FederalTax())}')
    print(f'Municipal = {calculator.calculate(budget, MunicipalTax())}')


if __name__ == '__main__':
    main()
