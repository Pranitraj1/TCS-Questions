def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i

    return -1

arr = list(map(int, input("Enter an array: ").split()))
key = int(input("Enter element to search: "))
result = linear_search(arr, key)

if result != -1:
    print(result)
else:
    print("Element not found")