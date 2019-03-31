class ListInfo:
    def __init__(self, li):
        self.list = li

    def add_key(self, key):
        self.list.append(key)

    def get_key(self, num):
        self.list.pop(num)

    def update_list(self, list):
        self.list.extend(list)

    def del_key(self, key):
        self.list.remove(key)
        self.list.sort()
        return self.list[len(self.list) - 1]


list_info = ListInfo([44, 222, 111, 333, 454, 'sss', '333'])

print(list_info.add_key("898"))

print(str(list_info))
