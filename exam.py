"""caling function inside a function"""
# def g():
#     print("Hi, it's me 'g'")
#     print("Thanks for calling me")
#
#
# def f(func):
#     print("Hi, it's me 'f'")
#     print("I will call 'func' now")
#     func()
#
#
# f(g)

"""class method"""
class student:
    school="admaren"
    def __init__(self,name):
        self.name=name

    @classmethod
    def my_school(cls):
        return cls.school
    @staticmethod
    def info():
        print("hi")

    def my_name(self):
        print(self.name)

