from abc import ABCMeta, abstractmethod


class Tax:
    __metaclass__ = ABCMeta

    def __init__(self, another_tax=None):
        self.__another_tax = another_tax

    def calculate_another_tax(self, budget):
        if self.__another_tax is None:
            return 0
        else:
            return self.__another_tax.calculate(budget)

    @abstractmethod
    def calculate(self, budget):
        pass


class TaxTemplate(Tax):
    __metaclass__ = ABCMeta

    def calculate(self, budget):
        if self.should_use_max_taxation(budget):
            return self.max_taxation(budget) + super(TaxTemplate, self).calculate_another_tax(budget)
        else:
            return self.min_taxation(budget) + super(TaxTemplate, self).calculate_another_tax(budget)

    @abstractmethod
    def should_use_max_taxation(self, budget):
        pass

    @abstractmethod
    def max_taxation(self, budget):
        pass

    @abstractmethod
    def min_taxation(self, budget):
        pass


class GlobalTax(TaxTemplate):
    def should_use_max_taxation(self, budget):
        return budget.value > 1000

    def max_taxation(self, budget):
        return budget.value * 0.01

    def min_taxation(self, budget):
        return budget.value * 0.2


class NationalTax(TaxTemplate):
    def should_use_max_taxation(self, budget):
        return budget.value > 500

    def max_taxation(self, budget):
        return budget.value * 0.02

    def min_taxation(self, budget):
        return budget.value * 0.1