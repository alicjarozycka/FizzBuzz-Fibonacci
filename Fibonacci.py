
def fibonacci(i):
    """
    Function name: Fibonacci
    Argument: i (number of numbers, expected type: integer)
    Returns: Depends on given i. If i equals 0, returns 0. If i equals 1 or 2, returns 1. In other cases it returns the sum of the preceding numbers.
    This function needs to be given i. If i value is less than 0, it returns "i cannot be a negative number".
    When i is equal to 0, it returns 0. When equal to 1 or 2, returns 1. In different cases, it returns number in which each number is the sum of the preceding ones.
    """

    if i < 0:
        return "i cannot be a negative number"

    elif i == 0:
        return 0

    elif i == 1 or i == 2:
        return 1

    else:
        return fibonacci(i - 1) + fibonacci(i - 2)


if __name__ == "__main__":

    start_number = int(input("Enter first number: "))
    end_number = int(input("Enter second number: "))

    if start_number < 1:
        print("First number should be greater or equal to 1.")
    elif start_number > end_number:
        print("First number should be less than second number")
    elif end_number > 250:
        print("Second number should be less or equal to 250")
    else:
        for i in range(start_number, end_number + 1):
            """
            I used loop for here in order to get results from specific range for Fibonacci sequence, which if defined by user.
            In that case, start_number should be greater or equal to 1 and less than end_number.
            End_number should be less or equal to 250.
            """
            print(fibonacci(i))



