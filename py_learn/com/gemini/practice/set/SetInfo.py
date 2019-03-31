class SetInfo:
    def __init__(self, set):
        self.set = set

    def add_set_info(self, keyname):
        self.set.add(keyname)

    def get_intersection(self, unioninfo):
        self.set.intersection(unioninfo)
        return self.set

    def get_union(self, unioninfo):
        self.set.union(unioninfo)
        return self.set

    def del_difference(self, unioninfo):
        self.set.difference(unioninfo)
        return self.set


set_info = SetInfo({'a', 'r', 'b', 'c', 'd'})

print(set_info)
set_info.add_set_info('8')
print(set_info)

