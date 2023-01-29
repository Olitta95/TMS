from random import randint
def binary_search(list, item):
    middle_index = len(list)//2
    low_index = 0
    higher_index = len(list)-1
    while list[middle_index] != item and low_index <= higher_index:
        if item > list[middle_index]:
            low_index = middle_index + 1
        else:
            higher_index = middle_index - 1
        middle_index = (low_index + higher_index)//2
    if low_index > higher_index:
        return None
    else:
        return middle_index
a = []
for i in range(10):
    a.append(randint(1, 20))
a.sort()
print(a)
value = int(input())
print(binary_search(a, value))
