"""method overloading"""
class student:

    def function(self,name=None):
        if name==None:
            print("none came")
        else:
            print("hi")

s1=student()
s1.function()