def merge_sorted_arrays(arr1, arr2):
    new_list = []
    for i in arr1:
        new_list.append(i)
    for i in arr2:
        new_list.append(i)

    x = sorted(new_list)
    return x


print(merge_sorted_arrays([0, 3, 4, 31], [3, 4, 6, 30,32]))


def merge_sorted_arrays(arr1,arr2):
    i = 0
    j = 0
    sorted_array = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_array.append(arr1[i])
            i += 1
        else:
            sorted_array.append(arr2[j])
            j += 1

    while i < len(arr1):
        sorted_array.append(arr1[i])
        i += 1

    while j < len(arr2):
        sorted_array.append(arr2[j])
        j += 1

    return sorted_array

print(merge_sorted_arrays([0, 3, 4, 5, 31], [3, 4, 7, 30, 32]))