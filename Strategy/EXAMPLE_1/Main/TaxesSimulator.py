from Strategy.EXAMPLE_1.Models.Budget import Budget
from Strategy.EXAMPLE_1.Models.Taxes import FederalTax, MunicipalTax
from Strategy.EXAMPLE_1.Models.Taxes_Calculator import TaxesCalculator


def main():
    calculator = TaxesCalculator()
    budget = Budget(500)
    print('Taxes:')
    print(f'Federal = {calculator.calculate(budget, FederalTax())}')
    print(f'Municipal = {calculator.calculate(budget, MunicipalTax())}')


if __name__ == '__main__':
    main()
