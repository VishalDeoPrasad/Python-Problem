def solve(ar):
    cnt = 0
    for i in range(len(ar)):
        for j in range(len(ar)):
            if ar[i] > ar[j]:
                cnt += 1
                break
    return cnt

def solve2(ar):
    total_max = ar.count(max(ar))
    cnt = len(ar) - total_max
    return cnt

print(solve([5,5,5,5,5,1]))
print(solve2([5,5,5,5,5,1]))
