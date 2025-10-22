"""This module implements a Luhn class for validating numbers using the Luhn algorithm."""

class Luhn:
    """A class to validate numbers using the Luhn algorithm."""

    def __init__(self, card_num):
        """Initialize the Luhn validator with a card number.
        
        :param card_num: The card number as a string
        :type card_num: str
        """
        self.card_num = card_num

    def valid(self) -> bool:
        """Validate the card number using the Luhn algorithm.
        
        :returns: True if the card number is valid, False otherwise
        :rtype: bool
        """
        # Validate input: only digits and spaces allowed
        if not all(c.isdigit() or c == ' ' for c in self.card_num):
            return False

        # Extract digits from the input
        digits = [int(c) for c in self.card_num if c.isdigit()]

        # Check for minimum length
        if len(digits) <= 1:
            return False

        # Process in reverse order and apply Luhn algorithm
        total_sum = 0
        for index, digit in enumerate(reversed(digits)):
            if index % 2 == 1:  # Double every second digit
                digit *= 2
                if digit > 9:  # Subtract 9 if the result is greater than 9
                    digit -= 9
            total_sum += digit

        return total_sum % 10 == 0
