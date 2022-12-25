arr = [1,2,3,4]
n = len(arr)
for i in range(n):
    for j in range(i+1, n):
        print(arr[i:j], end = " ")
    print()