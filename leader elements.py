"""Given an integer array A containing N distinct integers, you have to find all the leaders in array A.

An element is a leader if it is strictly greater than all the elements to its right side.

NOTE:The rightmost element is always a leader."""

def solve(A):
    leaderList = []
    '''for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] <= A[j]:
                break
        if j == len(A) -1:
            leaderList.append(A[i])
    return leaderList'''

    for i in range(0, len(A)):
        for j in range(i, len(A)):
            if (A[i] < A[j]):
                break
            if (j == len(A) - 1):
                leaderList.append(A[i])
       

print(solve([16, 17, 4, 3, 5, 2]))