class LinkedTuple:
    def __init__(self):
        self.items = list()

    # [("ksdkksdf8", "test"] -> [("ksdkksdfk", "test33")]

    def add(self, key, value):    # .add [("ksdkksdf8", "test"]

        # [("ksdkksdf8", "test"]
        # [("ksdkksdf8", "test"] -> [("ksdkksdfk", "test33")]
        self.items.append((key, value))

    def get(self, key):
        # ksdkksdf8
        # [("ksdkksdf8", "test"] -> [("ksdkksdfk", "test33")]
        for k, v in self.items:
            if key == k:
                return k


class LinkedDict:
    def __init__(self):
        self.items = [] # LinkedTuple
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        # LinkedTuple
        # []
        #
        self.items[index].add(key, value)
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))