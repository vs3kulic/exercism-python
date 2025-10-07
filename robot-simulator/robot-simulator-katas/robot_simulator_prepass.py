"""This module contains the pre-pass for a Robot class for simulating robot movements on a grid."""

# ----------------------------
# CONSTANTS
# ----------------------------
# Define the directions as constants


# ----------------------------
# REQUIREMENTS
# ----------------------------
# Robots are placed on a hypothetical infinite grid, facing a particular direction (north, east, south, or west) at a set of {x,y} coordinates, e.g., {3,8}, with coordinates increasing to the north and east.
# The robot then receives a number of instructions, at which point the testing facility verifies the robot's new position, and in which direction it is pointing.
# Example:
#   - The letter-string "RAALAL" means: Turn right, Advance twice, Turn left, Advance once, Turn left yet again
#   - Say a robot starts at {7, 3} facing north. Then running this stream of instructions should leave it at {9, 4} facing west.

# ----------------------------
# VALiDATIONS
# ----------------------------


# ----------------------------
# IMPLEMENTATION
# ----------------------------
# Define the mapping of directions to coordinate changes
# Create the Robot class with methods to turn and move
# Implement the instruction processing method
# Add error handling for invalid instructions