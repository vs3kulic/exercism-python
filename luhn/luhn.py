"""This module implements a Luhn class for validating numbers using the Luhn algorithm."""


class Luhn:
    """A class to validate numbers using the Luhn algorithm.
    
    The Luhn algorithm is used to validate various identification numbers,
    such as credit card numbers or IMEI numbers.
    """

    def __init__(self, card_num: str) -> None:
        """Initialize the Luhn validator with a card number.
        
        :param card_num: The card number as a string, which may include spaces
        :type card_num: str
        :returns: None
        :rtype: None
        """
        self.card_num = card_num

    def _normalize_input(self) -> str:
        """Remove spaces from the input string.
        
        :returns: String with all spaces removed
        :rtype: str
        """
        return self.card_num.replace(" ", "")

    def _validate_format(self, normalized: str) -> bool:
        """Check if the normalized string is a valid format for Luhn validation.
        
        :param normalized: String with spaces removed
        :type normalized: str
        :returns: True if format is valid (all digits, length > 1), False otherwise
        :rtype: bool
        """
        return len(normalized) > 1 and normalized.isdigit()

    def _convert_to_digits(self, normalized: str) -> list[int]:
        """Convert normalized string to a list of integers in reverse order.
        
        :param normalized: String with spaces removed
        :type normalized: str
        :returns: List of integers in reverse order for Luhn processing
        :rtype: List[int]
        """
        return [int(digit) for digit in reversed(normalized)]

    def _calculate_luhn_sum(self, digits: list[int]) -> int:
        """Calculate the Luhn checksum for a list of digits.
        
        :param digits: List of integers representing the digits of the number
        :type digits: List[int]
        :returns: The sum of all processed digits
        :rtype: int
        """
        total = 0
        for index, digit in enumerate(digits):
            if index % 2 == 1:  # Every second digit (0-indexed from right)
                digit *= 2
                if digit > 9:
                    digit -= 9
            total += digit
        return total

    def valid(self) -> bool:
        """Validate the card number using the Luhn algorithm.
        
        :returns: True if the card number is valid, False otherwise
        :rtype: bool
        """
        # Step 1: Normalize input (remove spaces)
        normalized = self._normalize_input()

        # Step 2: Validate format
        if not self._validate_format(normalized):
            return False

        # Step 3: Convert to digits in reverse order
        digits = self._convert_to_digits(normalized)

        # Step 4: Calculate Luhn sum and check validity
        luhn_sum = self._calculate_luhn_sum(digits)

        return luhn_sum % 10 == 0

def main() -> None:
    """Main function to demonstrate the Luhn class."""
    try:
        luhn_instance = Luhn("4539 1488 0343 6467")
        print("Card number is valid:", luhn_instance.valid())
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
