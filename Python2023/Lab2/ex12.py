def group_by_rhyme(list):
    dicti={}    
    for el in list:
        lst=el[len(el)-2]+el[len(el)-1]
        dicti.setdefault(lst,[]).append(el)
    return dicti

print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))