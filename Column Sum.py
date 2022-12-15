"""You are given a 2D integer matrix A, return a 1D integer array containing column-wise sums of original matrix."""

def solve(A):
    col_sum = []
    for i in range(len(A[0])):
        sum = 0
        for j in range(len(A)):
            sum += A[j][i]
            #print((j,i), end=" " )
        col_sum.append(sum)
    return col_sum

A = [[1,2,3,4], [5,6,7,8], [9,2,3,4]]
print("Columns wise summation =",solve(A))