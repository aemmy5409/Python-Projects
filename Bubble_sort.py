def sort(array: list):

    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def print_array(array: list):
    result = []
    for i in range(len(array)):
        result.append(array[i])
    print(result)


# implementation
myList = [8, 2, 4, 6, 7, 1, 5, 9, 3]
print("Original List: ")
print(myList)

print("\nOrdered List:")
sort(myList)
print_array(myList)
