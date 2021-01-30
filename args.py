"""multiple arguments/argumnet ,here we can give multiple actual argument and collect by using one *formal argument"""
def mysum(a,b):
    print(a+b)

mysum(10,22)
"""same can be done by using below method"""
def mylist(*integers):
    s=0
    for i in integers:
        s+=i
    print(s)

mylist(10,22,33,4,5,6,7,77)
