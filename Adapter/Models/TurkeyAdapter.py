class TurkeyAdapter:
    def __init__(self, turkey):
        self.__turkey = turkey

    def quack(self):
        self.__turkey.gobble()

    def fly(self):
        self.__turkey.fly()
