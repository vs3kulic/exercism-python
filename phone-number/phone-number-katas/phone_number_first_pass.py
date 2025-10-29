"""This module provides a PhoneNumber class for handling phone numbers."""
WHITELIST = set("()+-. ")
MIN_LENGTH = 10
MAX_LENGTH = 11


class PhoneNumber:
    """Class to represent and manipulate phone numbers."""
    def __init__(self, number):
        """Initialize the PhoneNumber instance with a number."""
        self.number = self._process_number(number)

    def _process_number(self, number: str) -> str:
        """Process the raw number: validate, clean, and return the cleaned number.
        
        :param number: The raw phone number input
        :type number: str
        :returns: The cleaned phone number
        :rtype: str
        :raises ValueError: If the number is invalid according to specified rules
        """
        # Validate characters and extract digits
        digits = []
        for char in number:
            if char.isalpha():
                raise ValueError("letters not permitted")
            if not (char.isdigit() or char in WHITELIST):
                raise ValueError("punctuations not permitted")
            if char.isdigit():
                digits.append(char)

        # Validate length
        if len(digits) < MIN_LENGTH:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) > MAX_LENGTH:
            raise ValueError("must not be greater than 11 digits")
        if len(digits) == MAX_LENGTH and digits[0] != "1":
            raise ValueError("11 digits must start with 1")

        # Clean the number
        if len(digits) == MAX_LENGTH and digits[0] == "1":
            digits = digits[1:]

        # Validate area and exchange codes
        area_code = digits[:3]
        exchange_code = digits[3:6]
        if area_code[0] == "0":
            raise ValueError("area code cannot start with zero")
        if area_code[0] == "1":
            raise ValueError("area code cannot start with one")
        if exchange_code[0] == "0":
            raise ValueError("exchange code cannot start with zero")
        if exchange_code[0] == "1":
            raise ValueError("exchange code cannot start with one")

        # Return the cleaned number
        return "".join(digits)

    @property
    def area_code(self):
        """Return the area code of the phone number."""
        return self.number[:3]

    def pretty(self):
        """Return the phone number in pretty format: (NXX) NXX-XXXX."""
        area_code = self.number[:3]
        exchange_code = self.number[3:6]
        subscriber_number = self.number[6:]
        return f"({area_code})-{exchange_code}-{subscriber_number}"