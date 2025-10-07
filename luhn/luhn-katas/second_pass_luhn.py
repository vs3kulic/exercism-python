"""This module implements a Luhn class for validating numbers using the Luhn algorithm."""

class Luhn:
    """A class to validate numbers using the Luhn algorithm."""
    def __init__(self, card_num: str):
        self.card_num = card_num

    def valid(self) -> bool:
        """Validate the card number using the Luhn algorithm."""
        # Iterate over the card_num string in reverse, collecting digits and ignoring spaces
        digits = []
        for char in reversed(self.card_num):
            if char == ' ':
                continue
            if not char.isdigit():
                return False
            digits.append(int(char))

        # Check for invalid input, return False if invalid (as per spec)
        if len(digits) <= 1:
            return False

        # Apply the Luhn algorithm
        total_sum = 0
        for index, digit in enumerate(digits):
            if index % 2 == 1:  # Double every second digit
                digit *= 2
                if digit > 9:  # Subtract 9 if the result is greater than 9
                    digit -= 9
            total_sum += digit  # Add the digit to total_sum
        return total_sum % 10 == 0

def main() -> None:
    """Main function to demonstrate the Luhn class."""
    try:
        luhn_instance = Luhn("4539 1488 0343 6467")
        print("Card number is valid:", luhn_instance.valid())
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
