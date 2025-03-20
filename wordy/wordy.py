"""
A module to answer word problems.
"""
from functools import reduce


OPERATIONS = {
    "plus": lambda left, right: left + right,
    "minus": lambda left, right: left - right,
    "multiplied_by": lambda left, right: left * right,
    "divided_by": lambda left, right: left / right
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
    Validate token values. Every second-even token (0, 2, 4, ...) should be a number;
    every second-odd token (1, 3, 5, ...) should be an operation

    param: tokens: list of tokens
    return None
    """
    # validate if there are tokens
    if tokens == []:
        raise ValueError("syntax error")

    # validate number tokens
    for index, number in enumerate(tokens[::2]):
        try:
            int(number)
        except ValueError as exc:
            if index == 0:
                if number in OPERATIONS:
                    raise ValueError("syntax error") from exc
                raise ValueError("unknown operation") from exc
            raise ValueError("syntax error") from exc

    # validate operation tokens
    for operation in tokens[1::2]:
        if operation not in OPERATIONS:
            if operation.isnumeric():
                raise ValueError("syntax error")
            raise ValueError("unknown operation")

    # after validating individual tokens, check overall structure of the expression
    if len(tokens) % 2 == 0:
        raise ValueError("syntax error")


def calculate_result(tokens: list[str]) -> int:
    """
    Calculate result of the tokens

    param: tokens: list of tokens
    return: result of the calculation
    """
    result = int(tokens[0])
    for index in range(1, len(tokens), 2):
        result = OPERATIONS[tokens[index]](result, int(tokens[index + 1]))
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
