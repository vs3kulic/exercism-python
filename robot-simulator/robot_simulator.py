"""This module simulates a robot moving on a grid."""

# Global variables for the directions
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

DIRECTION_DELTAS = [
    (0, 1),   # NORTH: y increases
    (1, 0),   # EAST: x increases
    (0, -1),  # SOUTH: y decreases
    (-1, 0)   # WEST: x decreases
]

class Robot:
    """A class to simulate a robot on a grid."""
    def __init__(self, direction = NORTH, x_pos: int = 0, y_pos: int = 0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)

    def move(self, instructions: str) -> None:
        """Move the robot based on the given instructions.
        
        :param instructions: A string, where 'R' = turn right, 'L' = turn left, 'A' = advance
        :type instructions: str
        :returns: None
        """
        for instruction in instructions:
            if instruction == "R":
                self._turn(1)
            elif instruction == "L":
                self._turn(-1)
            elif instruction == "A":
                self._advance()
            else:
                raise ValueError(f"Invalid instruction: {instruction}!")

    def _turn(self, step: int) -> None:
        """Turn the robot based on the given step.
        
        :param step: 1 for right turn, -1 for left turn
        :type step: int
        :returns: None
        """
        self.direction = (self.direction + step) % len(DIRECTION_DELTAS) # to avoid magic number

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
