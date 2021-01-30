"""decorator for swaping divison logic"""
def smartdiv(funct):
    def inner(c,d):
        if d==0:
            print("divison with 0 not allwed")
            c,d=d,c
        return funct(c,d)
    return inner


@smartdiv
def div(a,b):
    print(a/b)

div(2,7)
