def fizz_buzz(i):
    """
    Function name: fizz_buzz
    Argument: i (number, expected type: integer)
    Returns : Depends on what number is given to function. Returns 'FizzBuzz' when it can be divided by 5 or 3, 'Fizz' when divisible by 3,
    'Buzz' when divisible by 5 and in different cases, it just returns the number.
    This function needs to be given i, which is a number. If this number is divisible by 5 or 3, it returns "FizzBuzz".
    When given number can be divided by 3, it returns "Fizz". If 'i' is divisible by 5, it returns "Buzz". In other cases
    it simply returns given number.
    """

    if i % 15 == 0:
        return "FizzBuzz"

    elif i % 3 == 0:
        return "Fizz"

    elif i % 5 == 0:
        return "Buzz"

    else:
        return i


if __name__ == "__main__":

    start_number = int(input('Please enter first number: '))
    end_number = int(input('Please enter second number: '))

    if start_number < 1:
        print("First number should be greater or equal to 1.")
    elif start_number > end_number:
        print("First number should be less than second number")
    elif end_number > 10000:
        print("Second number should be less or equal to 10000")

    else:
        for i in range(start_number, end_number + 1):
            """
            I used loop for here, to get results from specific range, which if defined by user.
            In that case, start_number should be greater or equal to 1 and less than end_number.
            End_number should be less or equal to 10000.
            """
            print(fizz_buzz(i))



