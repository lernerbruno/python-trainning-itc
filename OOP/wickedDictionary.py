class WickedDictionary:
    def __init__(self):
        self.wicked_dict = {}

    def __repr__(self):
        return repr(self.wicked_dict)

    def __getitem__(self, key):
        return self.wicked_dict[key]

    def __setitem__(self, key, data):
        self.wicked_dict[2 * key] = data


my_dict = WickedDictionary()
my_dict['hello'] = 12
my_dict[2] = "test"
print(my_dict)
print(my_dict[4])
