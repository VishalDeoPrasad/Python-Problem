class Solution:
    # solve in O(n2)
    def solve1(self, A):
        for i in range(len(A)):
            cnt = 0
            for j in range(len(A)):
                if A[i] < A[j]:
                    cnt += 1    
            if cnt == A[i]:
                return 1
        return -1

    #solve in O(n)
    def solve(self, A):
        A.sort()
        n = len(A)
        for i in range(n - 1):
            if A[i] == A[i + 1]:
                continue #skip the next element
            if A[i] == n - i - 1: #how many element after this element
            #if A[i] == len(A[i+1:]):
                return 1
        
        if A[len(A) - 1] == 0: #if last element is 0 then return 1
            return 1
        return -1

print(Solution().solve([5,6,2]))