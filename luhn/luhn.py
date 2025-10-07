"""This module implements a Luhn class for validating numbers using the Luhn algorithm."""

class Luhn:
    """A class to validate numbers using the Luhn algorithm."""
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        """Validate the card number using the Luhn algorithm."""
        # Preprocess the input: replace spaces and strip leading or trailing spaces
        string = self.card_num.replace(" ", "").strip()

        # Check for invalid input, return False if invalid (as per spec)
        if len(string) <= 1 or not string.isdigit():
            return False

        # Convert string to a list of integers and reverse it
        digits = [int(digit) for digit in string]
        digits.reverse()

        # Apply the Luhn algorithm
        total_sum = 0
        for index, digit in enumerate(digits):
            if index % 2 == 1:  # Double every second digit
                digit *= 2
                if digit > 9:  # Subtract 9 if the result is greater than 9
                    digit -= 9
            total_sum += digit  # Add the digit to total_sum
        return total_sum % 10 == 0

def main():
    """Main function to demonstrate the Luhn class."""
    try:
        luhn_instance = Luhn("4539 1488 0343 6467")
        print("Card number is valid:", luhn_instance.valid())
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
