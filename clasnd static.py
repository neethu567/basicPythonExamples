"""class and static mehod"""
class student:
    clss="admaren"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def classmeth(cls,name,age):
        print(cls.clss)
        name="new neehu"
        age="new 33"
        print(name,age)

    @staticmethod
    def saticmeth(name,age):
        pass
        # print(name)
        # print(age)


s1=student("arjun",22)
s1.classmeth("nethu",22)
print(s1.name)
print(s1.age)
# s2=student("neethu",33)
# s2.saticmeth("name","age")
# print(s2.name)


