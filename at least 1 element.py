def solve(ar):
    cnt = 0
    for i in range(len(ar)):
        for j in range(len(ar)):
            if ar[i] > ar[j]:
                cnt += 1
                break
    return cnt

print(solve([9,5,2,2,8,8,9]))
