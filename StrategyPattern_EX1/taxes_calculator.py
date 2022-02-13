class TaxesCalculator(object):

    def calculate(self, budget, tax):
        calculated_tax = tax.calculate(budget)
        print(calculated_tax)
