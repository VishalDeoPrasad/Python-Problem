class Solution:
    def solve(self, A):
        total_sum = len(A)/2*(min(A)+max(A))
        return 1 if total_sum == sum(A) else 0

A = [3, 2, 1, 4, 5]
B = [1, 3, 2, 5]

print(Solution().solve(B))