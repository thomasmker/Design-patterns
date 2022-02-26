from ChainOfResponsability.EXAMPLE_1.Models.Budget import Budget, Item
from ChainOfResponsability.EXAMPLE_1.Models.Discount_Calculator import DiscountCalculator


def main():
    # No discount expected
    budget = Budget()
    budget.add_item(Item('Item A', 500.0))
    calculate_discount(budget)

    # Discount by value expected (1%)
    budget.add_item(Item('Item B', 100.0))
    calculate_discount(budget)

    # Discount by number of items expected  (10%)
    budget.add_item(Item('Item C', 400.0))
    budget.add_item(Item('Item D', 200.0))
    budget.add_item(Item('Item E', 300.0))
    budget.add_item(Item('Item F', 1000.0))
    calculate_discount(budget)


def calculate_discount(budget):
    discount_calculator = DiscountCalculator(budget)
    discount = discount_calculator.calculate()
    print(f'Total {budget.value}\nDiscount : {discount}\n')


if __name__ == '__main__':
    main()
