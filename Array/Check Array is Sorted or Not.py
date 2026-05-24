def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return ("Array is not sorted")

    return ("Array is sorted")

arr = list(map(int, input("Enter array elements: ").split()))
result = is_sorted(arr)
print(result)