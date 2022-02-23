from ChainOfResponsabilityPattern.EXAMPLE_1.Models.Discount import DiscountByFiveItems, DiscountByTotalOverFiveHundred, NoDiscount


class DiscountCalculator(object):
    def __init__(self, budget):
        self.__budget = budget

    def calculate(self):
        # The Design Pattern HERE
        discount = DiscountByFiveItems(
                    DiscountByTotalOverFiveHundred(
                    NoDiscount())
        ).calculate(self.__budget)

        return discount
