class Solution:
    def solve(self, A):
        for i in range(len(A)):
            cnt = 0
            for j in range(len(A)):
                if A[i] < A[j]:
                    cnt += 1    
            if cnt == A[i]:
                return 1
        return -1

print(Solution().solve([5,6,2]))