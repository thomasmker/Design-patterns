from StrategyPattern_EX2.Models.MallardDuck import MallardDuck
from StrategyPattern_EX2.Models.RubberDuck import RubberDuck


def main():
    mallard = MallardDuck()
    mallard.display()
    mallard.perform_quack()
    mallard.perform_fly()

    print(" --- ")

    mallard = RubberDuck()
    mallard.display()
    mallard.perform_quack()
    mallard.perform_fly()


if __name__ == '__main__':
    main()
