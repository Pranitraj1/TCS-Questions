def smallest_element(arr):
    smallest = arr[0]

    for num in arr:
        if num < smallest:
            smallest = num
    return smallest


arr = list(map(int, input("Enter an array: ").split()))
print(smallest_element(arr))1