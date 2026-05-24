def count_even_odd(arr):
    even = 0
    odd = 0

    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


arr1 = list(map(int, input("Enter array elements: ").split()))
result = count_even_odd(arr1)
print(result)