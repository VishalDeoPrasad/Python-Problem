class Solution:
    # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):
        if len(A) != len(A[0]):
            return 0
        
        for i in range(len(A)):
            for j in range(len(A)):
                print(A[i][j], end=" ")
            print()

        for i in range(len(A)):
            for j in range(len(A)):
                if i<j:
                    print("*", end="  ")
                else:
                    print(i,j, end="  ")

            print()
    

                
A = [
  [-459, 0, 0, 0, 0],
  [657, 816, 0, 0, 0],
  [914, 104, -166, 0, 0],
  [-94, 986, -733, 696, 0],
  [301, -682, -42, -11, -866]
]
print(Solution().solve(A))