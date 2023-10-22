def compose(note,sec,start):
    song=[]
    for i in sec:
        song.append(note[start])
        start=start+i
        start=start%len(note)
    song.append(note[start])
    return song

print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))