

def topen():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1

v=topen()
for i in v:
    print(i)