def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l) // 2; 
        if arr[mid] == x:                             # Check if x is present at mid 
            return mid  
        elif arr[mid] < x:                            # If x is greater, ignore left half 
            l = mid + 1 
        else:                                          # If x is smaller, ignore right half 
            r = mid - 1
    return -1                                          # If we reach here, then the element was not present 
  
arr = [ 2, 3, 4, 10, 40 ]                                   # Driver code
x = 10
result = binarySearch(arr, 0, len(arr)-1, x)                # Function call 
  
if result != -1: 
    print ("NUmber is at index % d" % result) 
else: 
    print ("Number is not present in array") 
