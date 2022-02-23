from abc import ABC


class Discount(ABC):
    def __init__(self, next_discount):
        self._next_discount = next_discount

    def calculate(self, budget):
        if self.is_discount_applicable(budget):
            return self.get_amount_discount(budget)
        else:
            return self._next_discount.calculate(budget)

    def is_discount_applicable(self, budget):
        return True

    def get_amount_discount(self, budget):
        return 0


class DiscountByFiveItems(Discount):
    def is_discount_applicable(self, budget):
        return budget.total_items > 5

    def get_amount_discount(self, budget):
        return budget.value * 0.1


class DiscountByTotalOverFiveHundred(Discount):
    def is_discount_applicable(self, budget):
        return budget.value > 500

    def get_amount_discount(self, budget):
        return budget.value * 0.01


class NoDiscount(Discount):
    def __init__(self):
        super().__init__(None)
