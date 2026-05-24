def array_sum(arr):
    total = 0

    for num in arr:
        total += num

    return total


arr = list(map(int, input("Enter an array: ").split()))
print(array_sum(arr))