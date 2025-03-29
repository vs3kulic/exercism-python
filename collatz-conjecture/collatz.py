def steps(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    def recursive_steps(num, counter=0):
        if num == 1:
            return counter
        if num % 2 == 0:
            return recursive_steps(num // 2, counter + 1)
        else:
            return recursive_steps(3 * num + 1, counter + 1)
    
    return recursive_steps(number)
