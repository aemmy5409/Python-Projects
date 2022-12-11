def collatz(number: int):

    # checks to see if "number" is odd or even
    if number % 2 == 0:
        result = number // 2
        print(result)
    elif number % 2 != 0:
        result = 3 * number + 1
        print(result)

    # loops and calls collatz(recursion) as long as the "result" is not 1
    while result != 1:
        collatz(result)
        break


# implementation
my_number = int(input("Enter a number: "))
collatz(my_number)
