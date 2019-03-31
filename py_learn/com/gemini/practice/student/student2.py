class Student2:
    def __init__(self, name, age, sex, address):
        self.name = name
        self.age = age
        self.sex = sex
        self.address = address

    def display(self):
        return "name={},age={},sex={},address={},".format(self.name, self.age, self.sex, self.address)


st = Student2("李四", 18, "男", "北京市朝阳区")

print(st.display())
