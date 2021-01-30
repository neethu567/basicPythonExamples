"""mixins for sharing a cls and methods of class  to another class"""
class a:
    total=1234

class m:
    def print(self):
        print(self.total)


class d(a,m):
    pass
class e(d):
    pass

E=e()
E.print()


