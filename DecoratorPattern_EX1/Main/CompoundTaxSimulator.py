from DecoratorPattern_EX1.Models.CompoundTaxCalculator import CompoundTaxCalculator
from DecoratorPattern_EX1.Models.Budget import Budget
from DecoratorPattern_EX1.Models.Taxes import GlobalTax, NationalTax

def main():
    calculator = CompoundTaxCalculator()
    budget = Budget(500)
    print('Taxes:')
    print(f'Global = {calculator.calculate(budget, GlobalTax())}')
    print(f'National = {calculator.calculate(budget, NationalTax())}')
    print(f'Compound = {calculator.calculate(budget, GlobalTax(NationalTax()))}')


if __name__ == '__main__':
    main()
