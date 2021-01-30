"""operator overloading"""
class car(object):
    def __init__(self,name,tyres):
        self.name=name
        self.tyres=tyres

    def __str__(self):
        return f"{self.tyres}"
    
    def __repr__(self):
        return f"{self.name}"

    def __add__(self, other):
        return car(f"{self.name}-{other.name}",self.tyres+other.tyres)








