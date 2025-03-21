"""
A module to answer word problems.
"""
from functools import reduce


OPERATIONS = {
    "plus": lambda x, y: x + y,
    "minus": lambda x, y: x - y,
    "multiplied_by": lambda x, y: x * y,
    "divided_by": lambda x, y: x // y
}


def get_tokens(question: str) -> list[str]:
    """
    Extract tokens from the question.

    param: question: str
    return: list of tokens
    """
    replacements = [
        ("What is", ""),
        ("?", ""),
        ("multiplied by", "multiplied_by"),
        ("divided by", "divided_by"),
    ]
 
    question = reduce(lambda q, rep: q.replace(rep[0], rep[1]), replacements, question)
    tokens = question.strip().split()

    return tokens


def validate_tokens(tokens: list[str]) -> None:
    """
    Validate token structure for math expressions.

    param: tokens: list of tokens
    return: None
    """
    # validate if there are tokens
    if not tokens:
        raise ValueError("syntax error")

    # validate number tokens
    for index, number in enumerate(tokens[::2]):
        try:
            int(number)
        except ValueError as exc:
            match (index == 0, number in OPERATIONS):
                case (True, True): # case 1
                    raise ValueError("syntax error") from exc
                case (True, False): # case 2
                    raise ValueError("unknown operation") from exc
                case (False, False): # case 3
                    raise ValueError("syntax error") from exc

    # validate operation tokens
    for operation in tokens[1::2]:
        match (operation in OPERATIONS, operation.isnumeric()):
            case (False, False): # case 1
                raise ValueError("unknown operation")
            case (True, True): # case 2
                raise ValueError("syntax error")
            case (False, True): # case 3
                raise ValueError("syntax error")

    # after validating individual tokens, check overall structure of the expression
    if len(tokens) % 2 == 0:
        raise ValueError("syntax error")


def calculate_result(tokens: list[str]) -> int:
    """
    Calculate result of the tokens

    param: tokens: list of tokens
    return: result of the calculation
    """
    result = int(tokens[0]) # start with first number in the expression as initial value
    numbers = [int(token) for token in tokens[2::2]] # extract numbers from the tokens
    operations = [OPERATIONS[tokens[i]] for i in range(1, len(tokens), 2)] # extract operations from the tokens

    for op, num in zip(operations, numbers):
        result = op(result, num)

    return result


def answer(question: str) -> int:
    """
    Answer the question

    param: question: str
    return int
    """
    tokens = get_tokens(question)
    validate_tokens(tokens) # calls for side-effects (raises exceptions)
    result = calculate_result(tokens)
    return result
