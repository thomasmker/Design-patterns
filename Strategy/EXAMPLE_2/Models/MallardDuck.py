from Strategy.EXAMPLE_2.Models.Duck import Duck
from Strategy.EXAMPLE_2.Behavior.Fly.FlyWithWings import FlyWithWings
from Strategy.EXAMPLE_2.Behavior.Quack.Quack import Quack


class MallardDuck(Duck):
    def __init__(self):
        fly_behavior = FlyWithWings()
        quack_behavior = Quack()
        super().__init__(fly_behavior, quack_behavior)


    def display(self):
        print("I'm real a mallard duck")