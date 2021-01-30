"""method overriding"""
class school:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getname(self):
        print(self.name)

class school2(school):
    def getname(self):
        print("hi")

s1=school("aaa",12)
s1.getname()
s2=school2("www",44)
s2.getname()