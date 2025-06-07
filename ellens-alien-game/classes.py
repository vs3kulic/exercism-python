"""Solution to Ellen's Alien Game exercise."""

class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Check if this Alien collides with another Alien.
    """
    total_aliens_created = 0  # Class variable to track the number of Alien instances created

    def __init__(self, x_coordinate=0, y_coordinate=0, health=3):
        """Initialize an Alien object with coordinates and health."""
        self.x_coordinate, self.y_coordinate = x_coordinate, y_coordinate
        self.health = health
        Alien.total_aliens_created += 1

    def hit(self):
        """Decrement Alien health by one point, ensuring it doesn't go below 0."""
        self.health = max(0, self.health - 1)

    def is_alive(self):
        """Return True if Alien health is greater than 0, otherwise False."""
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move Alien object to new coordinates."""
        self.x_coordinate, self.y_coordinate = new_x_coordinate, new_y_coordinate

    def collision_detection(self, other):
        """Check if this Alien collides with another Alien.

        Returns:
            True if the coordinates match, otherwise None.
        """
        if (self.x_coordinate, self.y_coordinate) == (other.x_coordinate, other.y_coordinate):
            return True
        return None

def new_aliens_collection(coordinates):
    """Create a list of Alien objects based on provided coordinates.

    param coordinates: list of tuples - Each tuple contains (x_coordinate, y_coordinate) for an Alien.
    :return: list - A list of Alien objects.
    """
    # Using list comprehension to create a list of Alien objects from the coordinates
    return [Alien(x_coordinate, y_coordinate) for x_coordinate, y_coordinate in coordinates]

    # -------------------------------------------------------------------------
    # Alternative implementation using a for loop (commented out for reference)
    # -------------------------------------------------------------------------
    # Initialize a list of new Alien objects
    # new_aliens = []

    # Loop through the coordinates and create an Alien object for each tuple
    # for x, y in coordinates:
    #    new_alien = Alien(x, y)

    # Append the newly created Alien object to the list
    #    new_aliens.append(new_alien)

    # return new_aliens
