class Solution:
    def sumi(self, a):
        result = 0
        for i in range(len(a)):
            result += a[i]
        return result
    
    def solve(self, A):
        if len(A) != len(A[0]):
            return 0
        
        for i in range(len(A)):
            if self.sumi(A[i]) != 1 or A[i][i] != 1:
                return 0
        return 1
a = [[0,1],[0,1]]
print(sum(a[0]))
print(Solution().solve(a))