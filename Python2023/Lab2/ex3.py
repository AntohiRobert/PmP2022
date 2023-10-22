def get_stuff(a,b):
    intersectie=[]
    reuniune=[]
    amb=[]
    bma=[]
    for i in a:
        reuniune.append(i)
        if i in b:
            intersectie.append(i)
        else:
            amb.append(i)
    for i in b:
        if i not in reuniune:
            reuniune.append(i)
        if i not in a:
            bma.append(i)
    return [intersectie,reuniune,amb,bma]

print(get_stuff([1,2,3],[3,4,5]))
    