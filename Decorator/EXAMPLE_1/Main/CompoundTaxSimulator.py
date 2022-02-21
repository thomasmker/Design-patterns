from Decorator.EXAMPLE_1.Models.CompoundTaxCalculator import CompoundTaxCalculator
from Decorator.EXAMPLE_1.Models.Budget import Budget
from Decorator.EXAMPLE_1.Models.Taxes import GlobalTax, NationalTax


def main():
    calculator = CompoundTaxCalculator()
    budget = Budget(500)
    print('Taxes:')
    print(f'Global = {calculator.calculate(budget, GlobalTax())}')
    print(f'National = {calculator.calculate(budget, NationalTax())}')
    print(f'Compound = {calculator.calculate(budget, GlobalTax(NationalTax()))}')


if __name__ == '__main__':
    main()
