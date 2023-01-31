def uniqueValue(ar):
    i, j = 1, 1
    while j < len(ar):     
        if ar[j-1] != ar[j]:
            ar[i] = ar[j]
            i += 1
        j += 1
    return ar[:i]

ar = [0,0,1,1,1,2,2,3,3,4]
print(uniqueValue(ar))