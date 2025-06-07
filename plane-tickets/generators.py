"""Functions to automate Conda airlines ticketing system."""

# Constants
SEATS_PER_ROW = 4

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.
    
    :requirements:
    - Seat letters are generated from A to D.
    - After D it should start again with A.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Example: A, B, C, D
    """
    for idx in range(number):
        # Calculate the ASCII value for the seat letter using modulo
        seat_letter = chr(65 + (idx % SEATS_PER_ROW))
        yield seat_letter
    
    # Alternatively we could use a generator expression:
    # return (chr(65 + (idx % SEATS_PER_ROW)) for idx in range(number))

def generate_seats(number):
    """Generate a series of identifiers for airline seats.
    
    :requirements:
    - There is no row 13. 
    - Each row has 4 seats.
    - A seat number consists of the row number and the seat letter.
    - Seats should be sorted from low to high.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    Example: 3C, 3D, 4A, 4B
    """
    row = 1

    while number > 0:
        if row == 13:  # Skip row 13
            row += 1
            continue
        for letter in generate_seat_letters(min(number, SEATS_PER_ROW)):
            yield f"{row}{letter}"
            number -= 1
        row += 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}
    """
    # Generate the required number of seats based on the number of passengers
    total_seats = len(passengers)
    seat_generator = generate_seats(total_seats)

    # Create an empty dictionary to store passenger-seat assignments
    passenger_seat_map = {}

    # Assign each passenger a seat by iterating through the passengers and the seat generator
    for passenger in passengers:
        seat = next(seat_generator) # Generate the next seat
        passenger_seat_map[passenger] = seat # Assign the seat to the passenger

    return passenger_seat_map

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    Example output: ['12AKL1022000', '38BKL1022000']
    """
    def create_ticket_code(seat, flight_id):
        """Helper function to create a single ticket code."""
        # Calculate the number of zeros needed to pad the ticket code to 12 characters
        padding_length = 12 - len(seat) - len(flight_id)
        padding = '0' * padding_length

        # Combine the seat number, flight ID, and padding to form the ticket code
        ticket_code = f"{seat}{flight_id}{padding}"
        return ticket_code

    # Use a generator to yield ticket codes for each seat number
    for seat in seat_numbers:
        yield create_ticket_code(seat, flight_id)
