"""This module provides a function to convert numbers into their spoken equivalent."""

ONES = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine"}
TEENS = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
TENS = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
        7: "seventy", 8: "eighty", 9: "ninety"}
GROUPS = {10**2: "hundred", 10**3: "thousand", 10**6: "million", 10**9: "billion"}

def say(number: int) -> str:
    """Convert a number into its spoken equivalent.
    
    param number: an integer between 0 and 999,999,999,999 inclusive.
    return: the spoken equivalent of the number as a string.
    """
    # Validate input
    if not 0 <= number <= 999_999_999_999:
        raise ValueError("input out of range")

    # Base case
    if number == 0:
        return "zero"

    # Handle simple cases (1-99)
    if number < 100:
        if number < 10:
            return ONES[number]
        if 10 <= number < 20:
            return TEENS[number]
        if 20 <= number < 100:
            ten, one = divmod(number, 10)
            return TENS[ten] + ("" if one == 0 else f"-{ONES[one]}")

    # Recursive case - find the largest group and recurse
    for value, group in sorted(GROUPS.items(), reverse=True):
        if number >= value:
            count, remainder = divmod(number, value)
            return say(count) + f" {group}" + ("" if remainder == 0 else " " + say(remainder))
    return ""

def main():
    """Main function to demonstrate the say function."""
    number = 100
    spoken = say(number)
    print(spoken)

if __name__ == "__main__":
    main()
