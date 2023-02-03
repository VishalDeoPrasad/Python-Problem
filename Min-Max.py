#Given an array of integers A and an integer B, 
# find and return the difference of B'th max element 
# and B'th min element of the array A.

class Solution:
    def solve(self, A, B):
        A.sort()
        max_elm = A[-B]
        min_elm = A[B-1]
        return max_elm - min_elm

print(Solution().solve([1, 2, 3, 4, 5], 2))