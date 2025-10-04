"""This module defines a Garden class that represents a kindergarten garden."""

STUDENTS = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Fred",
    "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"
]

PLANTS = {
    "R": "Radishes",
    "C": "Clover",
    "G": "Grass",
    "V": "Violets"
}

class Garden:
    """A class representing a kindergarten garden with students and their plants."""
    def __init__(self, diagram: str, students: list[str] = None) -> None:
        self.diagram = diagram
        self.students = sorted(students) if students else sorted(STUDENTS)

    def plants(self, student: str) -> list[str]:
        """Return the list of plants for the given student."""
        # Parse the diagram into rows, return list of strings
        rows = self.diagram.split("\n")

        # Find index of student in sorted list
        student_index = self.students.index(student)

        # Gather plants for both rows
        plants = []
        for row in rows:
            plant_indices = [2 * student_index, 2 * student_index + 1]
            for plant_index in plant_indices:
                plant_code = row[plant_index]
                plants.append(PLANTS[plant_code])
        return plants

def main():
    """Main function to demonstrate the Garden class."""
    garden = Garden("VC\nRC", ["Alice", "Bob"])
    print("Alice's plants:", garden.plants("Alice"))

if __name__ == "__main__":
    main()
