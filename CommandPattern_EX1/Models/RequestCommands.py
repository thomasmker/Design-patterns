from CommandPattern_EX1.Models.Command import Command


class RequestConclusion(Command):
    def __init__(self, request):
        self.__request = request

    def process(self):
        self.__request.conclude()


class RequestPayment(Command):
    def __init__(self, request):
        self.__request = request

    def process(self):
        self.__request.pay()
