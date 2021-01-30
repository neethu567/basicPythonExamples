"""multiple arguments/argumnet ,here we can give multiple actual argument as a list  and collect by using one formal argument by default it will take as list """

def mylist(integers):
    s=0
    for i in integers:
        s+=i
    print(s)

mylist([10,22,33,4,5,6,7,77])
