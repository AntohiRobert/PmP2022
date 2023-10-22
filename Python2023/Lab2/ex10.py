def tuples(lists):
    ans=[]
    mx=0
    for lst in lists:
        mx=max(mx,len(lst))
    for i in range(0,mx):
        curans=[]
        for lst in lists:
            curans.append(lst[i])
        ans.append(curans)
    return ans

print(tuples([[1,2,3], [5,6,7], ["a", "b", "c"]]))

