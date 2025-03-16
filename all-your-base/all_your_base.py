def rebase(input_base, digits, output_base):
    # check if the input base and output base are valid
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # check if the input digits are valid
    for d in digits:
        if d < 0 or d >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # convert the input digits to a number
    num = 0

    for d in digits:
        num = num * input_base + d # multiply the current number by the input base and add the current digit

    # convert the number to the output base
    output_digits = []

    while num > 0:
        output_digits.insert(0, num % output_base) # insert the remainder at the beginning of the list
        num //= output_base # update the number to be divided by the output base

    return output_digits or [0]