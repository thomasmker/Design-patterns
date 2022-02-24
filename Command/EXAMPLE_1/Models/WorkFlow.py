class WorkFlow:
    def __init__(self):
        self.__commands = []

    def add(self, command):
        self.__commands.append(command)

    def process(self):
        for command in self.__commands:
            command.process()
