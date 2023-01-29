def main():
    a = list(map(int,input().split()))
    N = a[0]
    B = int(input())
    A = a[1:] 
    B = B%N #normalize the B
    rotated_A = A[-B:]+A[:-B]
    for a in rotated_A:
        print(a, end=" ")
    return 0

if __name__ == '__main__':
    main()