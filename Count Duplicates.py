class Solution:
    def solve(self, A):
        return len(A)-len(set(A))

print(Solution().solve([1, 10, 20, 1, 25, 1, 10, 30, 25, 1] ))