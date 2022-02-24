from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def process(self):
        pass
