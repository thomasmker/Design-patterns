from budget import Budget
from taxes_calculator import TaxesCalculator
from taxes import FederalTax, MunicipalTax


def main():
    calculator = TaxesCalculator()
    budget = Budget(100)
    calculator.calculate(budget, FederalTax())
    calculator.calculate(budget, MunicipalTax())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

