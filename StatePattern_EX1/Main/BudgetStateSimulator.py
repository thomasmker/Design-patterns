from StatePattern_EX1.Models.Budget import Budget


def main():
    budget = Budget(500)
    print(budget.value)

    budget.apply_extra_discount()
    print(budget.value)

    budget.approve()
    budget.apply_extra_discount()
    print(budget.value)

    budget.close()


if __name__ == '__main__':
    main()