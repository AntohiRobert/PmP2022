def func(x=1, lst=[], flag=True):
    anslist=[]
    for st in lst:
        anslst=[]
        for c in st:
            fl=True
            if ord(c)%x==0:
                fl=False
            if (fl ^ flag):
                anslst.append(c)
        anslist.append(anslst)
    return anslist


print(func(x = 2, lst= ["test", "hello", "lab002"], flag = False))