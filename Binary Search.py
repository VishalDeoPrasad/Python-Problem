def BinarySearch(arr, key):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == key:
            return True
        
        if arr[mid] > key:
            right = mid-1
        elif arr[mid] < key:
            left = mid+1

    return False

print(BinarySearch([22,24,26,28,29,30,32,33,34,35], 22))