"""class method"""
import datetime
class Person:
    l='hhhh'
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def get_birthyear(cls,instance):

        # print(2021-s1.age)
        # print(2021-s2.age)
        print(2021-instance.age)
        cls.l='iiiii'
        print(cls.l)


    @staticmethod
    def school(age):
        # print(name,age,genter)
        print(2021-age)


        # print("i am neethu")
    def my_function(self):
        print(self.name)



s1=Person('neethu',24)
s2=Person("tom",22)
# Person.age=s1.age

Person.get_birthyear(s2)


# s1.my_function()
# # s2=Person.get_birthyear('anu',33)
# Person.get_birthyear()
# # s3=Person.school('tom',22,'female')
# Person.school(22)
# # print(s2.name)
