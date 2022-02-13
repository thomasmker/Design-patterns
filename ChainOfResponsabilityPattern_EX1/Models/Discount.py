from abc import ABC, abstractmethod


class DiscountBase(ABC):
    def __init__(self, next_discount):
        self._next_discount = next_discount

    def calculate(self, budget):
        if self.discount_condition(budget):
            return self.apply_discount(budget)
        else:
            return self._next_discount.calculate(budget)

    def discount_condition(self, budget):
        return True

    def apply_discount(self, budget):
        return 0


class DiscountByFiveItems(DiscountBase):
    def discount_condition(self, budget):
        return budget.total_items > 5

    def apply_discount(self, budget):
        return budget.value * 0.1


class DiscountByTotalOverFiveHundred(DiscountBase):
    def discount_condition(self, budget):
        return budget.value > 500

    def apply_discount(self, budget):
        return budget.value * 0.01


class NoDiscount(DiscountBase):
    def __init__(self):
        super().__init__(None)
