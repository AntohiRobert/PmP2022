def order_tuples(list):
    dicti=[]
    for tup in list:
        dicti.append((tup,tup[1][2]))
    dicti.sort(reverse=True)
    return dicti

print(order_tuples([('abc', 'bcd'), ('abc', 'zza')]))