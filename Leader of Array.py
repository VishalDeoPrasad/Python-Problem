def solve(A):
        leader = []
        leader.append(A[-1])
        max_elem = A[-1]
        for i in range(2, len(A)):
            if max_elem < A[-i]:
                leader.append(A[-i])
                max_elem = A[-i]
        return leader

print(solve([16,17,6,5,8,5,2]))