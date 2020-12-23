#O(n^2) brute force method but not scaleable, better answer available
array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i', 'x']

def list_intersection(array1, array2):
    for i in array1:
        for j in array2:
            if i == j:
                return True
    return False
print(list_intersection(array1, array2))

######################################################

# O(n)
def list_intersection(array1, array2):
    set_a = set(array1)
    for i in array2:
        if i in set_a:
            return True
    return False


print(list_intersection(array1, array2))
