array1 = [1, 7, 8, 4, 7, 7, 1]

def most_common_num(array1):
    most_common = 0  # which number happens the most often
    max_occur = 0 # max number of times an item occurs

    for num in array1:
        count = 0
        for number in array1:
            if number == num:
                count += 1  # counts the amount of times num happens
                if count > max_occur:
                        max_occur = count
                        most_common = num

    return most_common

print(most_common_num(array1))

#######################################################

array1 = [1, 7, 8, 4, 7, 7, 1]

def most_common_num(array1):
    most_common = 0  # which number happens the most often
    max_occur = 0 # max number of times an item occurs
    array_dict = {} # stores a value, adds to value if it occurs again
    for num in array1:
        if num in array_dict:
            array_dict[num] += 1
        else:
            array_dict[num] = 1
    for number, count in array_dict.items():
        if count > max_occur:
            max_occur = count
            most_common = number
    return most_common


print(most_common_num(array1))

#time complexity n(log n)
#space complexity n(c)