from TemplatePattern_EX1.Models.Budget import Budget
from TemplatePattern_EX1.Models.NewTaxesCalculator import NewTaxesCalculator
from TemplatePattern_EX1.Models.TaxTemplate import GlobalTax,NationalTax

def main():
    calculator = NewTaxesCalculator()
    budget = Budget(500)
    print('Taxes:')
    print(f'Global = {calculator.calculate(budget, GlobalTax())}')
    print(f'National = {calculator.calculate(budget, NationalTax())}')


if __name__ == '__main__':
    main()