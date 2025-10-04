"""This module defines a Garden class that represents a kindergarten garden."""

STUDENT_NAMES = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Fred",
    "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"
]

DIAGRAM_ENCODING = {
    "R": "Radishes",
    "C": "Clover",
    "G": "Grass",
    "V": "Violets"
}

class Garden:
    """A class representing a kindergarten garden with students and their plants."""
    def __init__(self, diagram: str, students: list[str]) -> None:
        self.diagram = diagram
        self.students = sorted(students) if students else sorted(STUDENT_NAMES)

    def plants(self, student: str) -> list[str]:
        """Return the list of plants for the given student."""
        rows = self.diagram.split("\n") # split diagram into rows, returns list of strings
        student_index = self.students.index(student) # find index of student in sorted list

        plants = []
        # TODO: calculate plant indices, stores as list of integers
        # TODO: gather plants for both rows
        return plants
