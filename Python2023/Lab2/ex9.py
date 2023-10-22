def cnt_see(matrix):
    tuples=[]
    mx=[]
    i=0
    for lst in matrix:
        if i==0:
            for el in lst:
                mx.append(el)
        else:
            for j in range(0,len(lst)-1):
                if (lst[j]<=mx[j]):
                    tuples.append((i,j))
                else:
                    mx[j]=lst[j]
        i=i+1
    return tuples

print(cnt_see([[1, 2, 3, 2, 1, 1],[2, 4, 4, 3, 7, 2],[5, 5, 2, 5, 6, 4],[6, 6, 7, 6, 7, 5]] ))