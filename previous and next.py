class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        new_A = []
        for i in range(len(A)): # 0, 1, 2, 3, 4
            if i == 0:
                #A[i] = A[i]*A[i+1]
                if len(A) == 1:
                    return A
                new_A.append(A[i]*A[i+1])
            elif i == len(A)-1:
                #A[i] = A[i]*A[i-1]
                new_A.append(A[i]*A[i-1])
            else:
                #A[i] = A[i-1]*A[i+1]
                new_A.append(A[i-1]*A[i+1])
        return new_A
A = [1, 2, 3, 4, 5]
print(Solution().solve(A))