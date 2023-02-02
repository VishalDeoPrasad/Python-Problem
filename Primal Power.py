import math
class Solution:
    # @param A : list of integers
    # @return an integer
    def prime_number(self, n):
        if n > 1:
            for i in range(2, int(math.sqrt(n))+1):
                if n%i == 0:
                    break
            else:
                return 1
        return 0

    def solve(self, A):
        cnt = 0
        for n in A:
            if n > 1:
                cnt += self.prime_number(n)
        return cnt

print(Solution().solve([11, 3, 1]))
