class LimitedList:

    def __init__(self, max_length):
        self.max_length = max_length
        self.limited_list = []

    def __repr__(self):
        return str(self.limited_list)

    def __getitem__(self, key):
        return self.limited_list[key]

    def __setitem__(self, list_index, data):
        self.limited_list[list_index] = data

    def append(self, element):
        if len(self.limited_list) < self.max_length:
            self.limited_list.append(element)
        else:
            del self.limited_list[0]
            self.limited_list.append(element)


my_list = LimitedList(3)
print(my_list)
my_list.append(5)
my_list.append(2)
my_list.append(10)
print(my_list)
my_list.append("hello")
print(my_list)
my_list[1] = "changed"
print(my_list)
