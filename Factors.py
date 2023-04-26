class FindFactors:
    #Solution1 - TC - O(N), SC - O(N)
    #Total iteration = N
    def Factor1(self,n):
        factor = []
        for i in range(1, n+1):
            if n%i == 0:
                factor.append(i)
        return factor
    
    #Solution2 - TC - O(N), SC - O(N)
    #Total iteration = N/2
    def Factor2(self,n):
        factor = []
        for i in range(1, n//2+1):
            if n%i == 0:
                factor.append(i)
        factor.append(n)
        return factor
    
    #Solution3 - TC - O(sqrt(N)), SC - O(N)
    #Total iteration = sqrt(n)
    def Factor3(self, number):
        factors = []
        factors.append(1)
        # check if 2 is a factor of the number
        if number % 2 == 0:
            factors.append(2)
            factors.append(number//2)
        # loop from 3 to the square root of the number, incrementing by 2
        for i in range(3, int(number**0.5)+1):
            # if i is a factor of number, add it to the factors list
            if number % i == 0:
                factors.append(i)
                factors.append(number//i)
        # append the number itself to the factors list
        factors.append(number)
        factors.sort()
        return factors
    
    def Factor4(self, number):
        factors = []
        # loop from 1 to the square root of the number
        for i in range(1, int(number**0.5)+1):
            # if i is a factor of number, add it to the factors list
            if number % i == 0:
                factors.append(i)
                factors.append(number//i)
        
        factors.sort()
        return factors
print(FindFactors().Factor1(28))
print(FindFactors().Factor2(28))
print(FindFactors().Factor3(28))
print(FindFactors().Factor4(28))
