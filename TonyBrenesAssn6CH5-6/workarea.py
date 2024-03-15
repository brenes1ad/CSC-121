def sum2d(array):
    sum = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            sum += array[i][j]
    return sum

listOfLists = [list(range(i, i+10)) for i in range(1,100,10)]

print(listOfLists)
print(sum2d(listOfLists))