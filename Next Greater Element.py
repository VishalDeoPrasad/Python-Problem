def GreaterElement(arr):
    dic = {}
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                dic[arr[i]] = arr[j]
                break
            if j == len(arr)-1:
                dic[arr[i]] = -1
    dic[arr[i]] = -1
    return dic
arr1 = [6,5,4,3,2,1,7]
arr = [5,25,10,8,6,12,9,18]
print(arr)
print(GreaterElement(arr1))
