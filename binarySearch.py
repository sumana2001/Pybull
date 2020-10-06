# Find first position of a value in sorted array or determine if it not in it
def find(value, arr):
    l = -1
    r = len(arr)
    ans = -1
    while r - l > 1:
        mid = (r + l) // 2
        if (value >= arr[mid]):
            r = mid
            if (value == arr[mid]):
                ans = mid
        else:
            l = mid
    return ans


            
