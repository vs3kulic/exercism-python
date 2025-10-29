"""This module provides a PhoneNumber class for handling phone numbers."""
CHAR_WHITELIST = frozenset("()+-. ") # whitelisted characters
MIN_LENGTH = 10
MAX_LENGTH = 11
ACL = 3 # Area Code Length
ECL = 3 # Exchange Code Length


class PhoneNumber:
    """Class to represent and manipulate phone numbers."""
    def __init__(self, number: str):
        """Initialize the PhoneNumber instance with a number."""
        self._cleaned_number = self._process_number(number)

    def _process_number(self, number: str) -> str:
        """Pipeline to orchestrate the phone number processing.
        
        :param number: The raw phone number input
        :type number: str
        :returns: The cleaned phone number
        :rtype: str
        """
        self._validate_characters(number)
        cleaned_number = self._extract_digits(number)
        self._validate_length(cleaned_number)
        self._validate_codes(cleaned_number)
        return cleaned_number

    # Check for invalid characters
    def _validate_characters(self, number: str) -> None:
        """Find and raise errors for invalid characters in the phone number."""
        for char in number:
            if char.isalpha():
                raise ValueError("letters not permitted")
            if not (char.isdigit() or char in CHAR_WHITELIST):
                raise ValueError("punctuations not permitted")

    # Extract and clean digits
    def _extract_digits(self, number: str) -> str:
        """Extract digits and handle leading '1'."""
        cleaned_number = "".join(char for char in number if char.isdigit())
        if len(cleaned_number) == 11 and cleaned_number[0] == "1":
            return cleaned_number[1:]  # Remove leading '1'
        return cleaned_number

    # Validate the length of raw digits
    def _validate_length(self, cleaned_number: str) -> None:
        """Validate the cleaned number for length."""
        if len(cleaned_number) < MIN_LENGTH:
            raise ValueError(f"must not be fewer than {MIN_LENGTH} digits")
        if len(cleaned_number) > MAX_LENGTH:
            raise ValueError(f"must not be greater than {MIN_LENGTH} digits")

    # Validate area and exchange codes
    def _validate_codes(self, cleaned_number: str) -> None:
        """Validate area code and exchange code rules."""
        area_code = cleaned_number[:3]
        exchange_code = cleaned_number[3:6]

        if area_code[0] == "0":
            raise ValueError("area code cannot start with zero")
        if area_code[0] == "1":
            raise ValueError("area code cannot start with one")
        if exchange_code[0] == "0":
            raise ValueError("exchange code cannot start with zero")
        if exchange_code[0] == "1":
            raise ValueError("exchange code cannot start with one")

    @property
    def number(self) -> str:
        """Return the cleaned phone number as a string of digits."""
        return self._cleaned_number

    @property
    def area_code(self) -> str:
        """Return the area code of the phone number."""
        return self._cleaned_number[:3]

    def pretty(self) -> str:
        """Return the phone number in pretty format: (NXX) NXX-XXXX."""
        area_code = self._cleaned_number[:ACL]
        exchange_code = self._cleaned_number[ACL:(ACL+ECL)]
        subscriber_number = self._cleaned_number[(ACL+ECL):]

        return f"({area_code})-{exchange_code}-{subscriber_number}"


def main():
    """Main function to demonstrate the PhoneNumber class."""
    phone = PhoneNumber("(223) 456-7890")
    print(f"Cleaned number: {phone.number}")
    print(f"Area code: {phone.area_code}")
    print(f"Pretty format: {phone.pretty()}")

if __name__ == "__main__":
    main()
