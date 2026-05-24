def merge_two_arrays(arr1, arr2):
    arr = arr1 + arr2
    return arr

arr1 = list(map(int, input("Enter an array: ").split()))
arr2 = list(map(int, input("Enter an array: ").split()))
result = merge_two_arrays(arr1, arr2)
print("Merging two arrays")
print(result)