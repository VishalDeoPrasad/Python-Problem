class Solution:
    def solve(self, A):
        if len(A) != len(A[0]):
            return 0
        
        for i in range(len(A)):
            for j in range(len(A)):
                if i < j:
                    if A[i][j] != 0:
                        return 0
        return 1
A = [[1, 0, 0],
      [0, 0, 0],
      [-7, -8, 9]]
print(Solution().solve(A))