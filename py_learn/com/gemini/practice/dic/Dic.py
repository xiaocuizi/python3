# 字典类似于JSON dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
class Dic:
    def __init__(self, e):
        self.e = e

    def del_dict(self, key):
        del self.e[key]

    def get_dict(self, key):
        if key in self.e:
            return self.e[key]
        else:
            return "Sorry the key not found"

    def update_dict(self, dic):
        if isinstance(self.e, dict) and isinstance(dic, dict):
            self.e.update(dic)
            return self.e.values()


dic = Dic({'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'})

print(dic.get_dict('Alice'))

print(dic.del_dict('Beth'))
print(dic.get_dict('Beth'))

print(dic.update_dict({'Dlice': '12343', 'Eeth': '5656', 'Fecil': '787878'}))
