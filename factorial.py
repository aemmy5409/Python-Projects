def factorial(num: int):
    base_number = 1

    # changes the value of base_number after every iteration and multiplies by the next number
    for number in range(1, num+1):
        base_number = base_number * number

    return base_number


# implementation
number = int(input("Enter a number: "))
print(factorial(number))
