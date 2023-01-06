def subString(s):
    sub_str = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub_str.append(s[i:j])
    return sub_str
    
s = 'flower'
print(subString(s))