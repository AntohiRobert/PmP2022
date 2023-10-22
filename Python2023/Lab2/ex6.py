def ret_freq(lists,freq):
    mp=dict()
    for list in lists:
        for elem in list:
            if elem in mp:
                mp[elem]=mp[elem]+1
            else:
                mp[elem]=1
    anslist=[]
    for elem in mp:
        if mp[elem]==freq:
            anslist.append(elem)
    return anslist

testlist=[[1,2,3], [2,3,4],[4,5,6], [4,1, "test"]]
print(ret_freq(testlist,2))