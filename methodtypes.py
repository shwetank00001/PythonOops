class student():

    school='KV IFFCO'

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def details():
        return "Hello"

s1=student(45,14,15)
s2=student(91,71,12)



print(student.info())
print(s1.avg())
print(student.details())