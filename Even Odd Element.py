def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    for _ in range(T):
        a = list(map(int,input().split()))
        n = a[0]
        ar = a[1:] 
        even_sum = 0
        odd_sum = 0
        for i in range(n):
            if ar[i]%2 == 0:
                even_sum += 1
            else:
                odd_sum += 1
        print(abs(even_sum-odd_sum))
    return 0

if __name__ == '__main__':
    main()