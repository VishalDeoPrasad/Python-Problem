from collections import Counter
def commonStr(s1, s2):
    print(Counter(s1))
    print(Counter(s2))
    print(Counter(s1)-Counter(s2))
    unique_char = set(s1)
    cnt = 0
    for ch in unique_char:
        if s1.count(ch) == s2.count(ch):
            cnt += 1
    return cnt
s = "fdhlvosfpafhalll"
n = len(s)
s1 = s[:n//2]
s2 = s[n//2:]
print(commonStr(s1, s2))