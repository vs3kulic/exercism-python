def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if not isinstance(number, int) or number < 1:
        raise ValueError('Please enter a positive integer.')

    divisors = [i for i in range(1, number) if number % i == 0]

    aliquot_sum = sum(divisors)

    if aliquot_sum == number:
        return 'perfect'
    elif aliquot_sum < number:
        return 'deficient'
    else:
        return 'abundant'
