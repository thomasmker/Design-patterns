class Budget(object):
    def __init__(self):
        self.__items = []

    @property
    def value(self):
        total = sum(item.value for item in self.__items)
        return total

    @property
    def total_items(self):
        return len(self.__items)

    def get_items(self):
        return tuple(self.__items)

    def add_item(self, item):
        self.__items.append(item)


class Item(object):
    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    @property
    def value(self):
        return self.__value

    @property
    def name(self):
        return self.__name
