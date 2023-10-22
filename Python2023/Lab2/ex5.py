def setzero(matrix):
    ansmatrix=[]
    i=0
    for row in matrix:
        ansrow=[]
        j=0
        for elem in row:
            if j<i:
                ansrow.append(0)
            else:
                ansrow.append(elem)
            j=j+1
        ansmatrix.append(ansrow)
        i=i+1
    return ansmatrix


my_array = [ 
    [1, 2, 3,10], 
    [4, 5, 6,10], 
    [7, 8, 9,10],
    [1,2,3,4] 
]

newm=setzero(my_array)

print(newm)