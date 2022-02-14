from abc import ABCMeta, abstractmethod


class TaxTemplate:
    __metaclass__ = ABCMeta

    def calculate(self, budget):
        if self.should_use_max_taxation(budget):
            return self.max_taxation(budget)
        else:
            return self.min_taxation(budget)

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