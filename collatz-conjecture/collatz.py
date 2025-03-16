def steps(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    counter = 0
    while number != 1: 
        if number % 2 == 0: 
            number = number // 2
        else:
            number = 3 * number + 1
        counter += 1
    return counter