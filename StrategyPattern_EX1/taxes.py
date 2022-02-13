class FederalTax(object):
    def calculate(self, budget):
        return budget.value * 0.1


class MunicipalTax(object):
    def calculate(self, budget):
        return budget.value * 0.06
