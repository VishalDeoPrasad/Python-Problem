def subString(s):
    sub_str = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            sub_str.append(s[i:j])
    return sub_str

def Total_subString(lst):
    subString_list = []
    for str in lst:
        subString_list.extend(subString(str))
    return subString_list

subString = Total_subString(['flower', 'flow', 'flight'])
print(subString)

