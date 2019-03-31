class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        score_tem = self.score;
        if score_tem is not None:
            if isinstance(score_tem, list):
                score_tem.sort()
                return score_tem[len(score_tem) - 1]


zm = Student('zhangming', 20, [88, 69, 100])
print(zm.get_name())
print(zm.get_age())
print(zm.get_course())
