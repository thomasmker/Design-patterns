from abc import ABC, abstractmethod


class CustomOperation(ABC):

    @abstractmethod
    def calculate(self):
        pass
