def mykwrdarg(**integers):
    fullname=""
    for i in integers.values():
        fullname+=i
    print(fullname)

mykwrdarg(firstname="aaaa",lastname="bbbbb")



