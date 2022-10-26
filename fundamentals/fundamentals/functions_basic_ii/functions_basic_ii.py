#1 Countdown

def countdown(num):
    countdownList = []
    for i in range(num, -1, -1):
        countdownList.append(i)
    return countdownList
print(countdown(8))


# 2 Print and Return

def print_and_return(list):
    print(list[0])
    return list[1]
print (print_and_return([3,12]))


#3 First Plus Length

def first_plus_length(list):
    x = list[0] + len(list)
    return x
print (first_plus_length([14,6,9]))


# 4 Values Greater than Second

def values_greater_than_second(list):
    if len(list) < 2:
        return False

    newList = []
    for x in list:
        if x > list[1]:
            newList.append(x)
    print(len(newList))
    return newList
print(values_greater_than_second([222,11,33,44,55,9]))
print(values_greater_than_second([1]))


#5 This Length, That Value

def length_and_value(size,value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList
print(length_and_value(8,12))
