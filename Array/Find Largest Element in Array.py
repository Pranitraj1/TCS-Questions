def largest_element(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num



    return largest


arr = list(map(int, input("Enter an array: ").split()))
print(largest_element(arr))
