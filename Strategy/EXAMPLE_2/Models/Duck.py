from abc import ABC, abstractmethod


class Duck(ABC):
    def __init__(self, fly_behavior, quack_behavior):
        self.__flyBehavior = fly_behavior
        self.__quackBehavior = quack_behavior

    @abstractmethod
    def display(self):
        pass

    def perform_fly(self):
        self.__flyBehavior.fly()

    def perform_quack(self):
        self.__quackBehavior.quack();

    def swim(self):
        print("Splash splash, all ducks float, even decoys!")
