# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # Check if x is present at mid
        if arr[mid] < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid] > x:
            high = mid - 1

        # If x is smaller, ignore right half
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


if __name__ == "__main__":
    size = int(input("Enter the size of array : "))
    array = []
    print("Enter the array values")
    for i in range(0, size):
        ele = int(input("Enter element and press enter: "))
        array.append(ele)  # adding the element

    n = int(input("Enter number to search : "))

    result = binary_search(array, n)

    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")
