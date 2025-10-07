"""This module simulates a robot moving on a grid."""

# Global variables for the directions
NORTH = "NORTH"
EAST = "EAST"
WEST = "WEST"
SOUTH = "SOUTH"

# Coordinate changes for each direction
DIRECTION_DELTAS = {
    NORTH: (0, 1),  # y increases (north)
    SOUTH: (0, -1), # y decreases (south)
    EAST: (1, 0),   # x increases (east)
    WEST: (-1, 0)   # x decreases (west)
}

DIRECTIONS_LEFT = {
    NORTH: WEST,
    WEST: SOUTH,
    SOUTH: EAST,
    EAST: NORTH
}

DIRECTIONS_RIGHT = {
    NORTH: EAST,
    EAST: SOUTH,
    SOUTH: WEST,
    WEST: NORTH
}

class Robot:
    """A class to simulate a robot on a grid."""
    def __init__(self, direction: str=NORTH, x_pos: int=0, y_pos: int=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions: str) -> None:
        """Move the robot based on the given instructions."""
        for instruction in instructions:
            if not instruction in "RLA":
                raise ValueError(f"Invalid instruction: {instruction}. Valid instructions: 'R', 'L', and 'A'.")
            if instruction == "R":
                self._turn_right()
            if instruction == "L":
                self._turn_left()
            if instruction == "A":
                self._advance()

    def _turn_right(self) -> None:
        """Turn the robot 90 degrees to the right."""
        # Update the robot's direction
        self.direction = DIRECTIONS_RIGHT[self.direction]

    def _turn_left(self) -> None:
        """Turn the robot 90 degrees to the left."""
        self.direction = DIRECTIONS_LEFT[self.direction]

    def _advance(self) -> None:
        """Move the robot one unit forward in the direction it is currently facing."""
        x, y = self.coordinates
        dx, dy = DIRECTION_DELTAS[self.direction]
        self.coordinates = (x + dx, y + dy)

def main():
    """Main function to demonstrate the Robot class."""
    robot = Robot(NORTH, 8, 4)
    print(f"Robot's initial position: {robot.coordinates}, facing {robot.direction}")
    robot.move("LAAARRRALLLL")
    print(f"Robot's final position: {robot.coordinates}, facing {robot.direction}")

if __name__ == "__main__":
    main()
