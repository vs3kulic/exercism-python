"""This module implements a simple grade school roster management system."""
import bisect

class School:
    """The School class manages students and their grades."""
    def __init__(self):
        self.students = []  # Sorted list of (grade, name) tuples
        self.add = []

    def add_student(self, name: str, grade: int) -> None:
        """Add a student to the school roster.
        
        :param name: The student's name
        :type name: str
        :param grade: The student's grade
        :type grade: int
        :returns: None
        """
        # Check if the student is already in the school
        if any(student_name == name for _, student_name in self.students):
            self.add.append(False)
        else:
            # Insert the student - the list is kept sorted by (grade, name)
            bisect.insort(self.students, (grade, name))
            self.add.append(True)

    def added(self):
        """Track which students were successfully added."""
        return self.add.copy()

    def roster(self) -> list:
        """List all the students in the school in order."""
        # Extract names from the sorted list of (grade, name) tuples
        return [name for _, name in self.students]

    def grade(self, grade_number: int) -> list:
        """Return a sorted list of students for specified grade.
        
        :param grade_number: The grade number
        :type grade_number: int
        :returns: A sorted list of student names in the specified grade
        :rtype: list
        """
        # Filter the students list for the specified grade
        return [name for grade, name in self.students if grade == grade_number]

def main():
    """Main function to demonstrate the School class."""
    school = School()
    school.add_student(name="Blair", grade=3)
    school.add_student(name="James", grade=3)
    school.add_student(name="Ron", grade=5)
    school.add_student(name="Paul", grade=5)
    print(f"Students in grade 3: {school.grade(3)}")
    print(f"Students in grade 5: {school.grade(5)}")
    print(f"Addition results: {school.added()}")
    print(f"Full roster: {school.roster()}")

if __name__ == "__main__":
    main()
