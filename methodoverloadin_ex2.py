"""methd overloading"""
class area:
    def findarea(self,l=None,b=None):
        if b==None:
            print("area of square")
            print(l*l)
        else:
            print("areaof rectangle")
            print(l*b)
a=area()
a.findarea(10,22)
