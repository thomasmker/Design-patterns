from Strategy.EXAMPLE_2.Models.Duck import Duck
from Strategy.EXAMPLE_2.Behavior.Fly.FlyNoWay import FlyNoWay
from Strategy.EXAMPLE_2.Behavior.Quack.Squeak import Squeak


class RubberDuck(Duck):
    def __init__(self):
        fly_behavior = FlyNoWay()
        quack_behavior = Squeak()
        super().__init__(fly_behavior, quack_behavior)


    def display(self):
        print("I'm a rubber duck")