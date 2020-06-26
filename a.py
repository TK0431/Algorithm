def binary_search(list, item):
    low = 0
    heigh = len(list) - 1
    while low <= heigh:
        mid = int((low + heigh) / 2)
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            heigh = mid -1
        else:
            low = mid + 1
    return None

mylist = [1,3,5,7,9]
print(binary_search(mylist,2))