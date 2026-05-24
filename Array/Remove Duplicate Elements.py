def remove_duplicates(arr):
    result = []

    for num in arr:
        if num not in result:
            result.append(num)

    return result


arr = list(map(int, input("Enter array elements: ").split()))
print(remove_duplicates(arr))