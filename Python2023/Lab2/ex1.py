def first_n_fib(n):
    a=0
    b=1
    list=[0,1]
    for i in range(2,n):
        c=a+b
        list.append(c)
        a=b
        b=c
    return list

print(first_n_fib(4))