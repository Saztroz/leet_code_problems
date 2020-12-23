#naive approach

def first_Recurring(arr):
    min_dist = len(arr)
    value = arr[0]
    recurringFound = False

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                distance = j - i
                if distance < min_dist:
                    min_dist = distance
                    value = arr[i]
                    recurringFound = True
    if recurringFound:
        return value
    else:
        return 'Undefined'


print(first_Recurring([2,5,2,5,3,1,4]))



def first_recurring_character(input: list):
    seen = {}
    for i in input:
        if i in seen:
            return i
        else:
            seen[i] = i
    return None


print(first_recurring_character([2,5,1,2,3,5,1,2,4]))