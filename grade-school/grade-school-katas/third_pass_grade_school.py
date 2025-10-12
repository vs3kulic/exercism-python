"""This module implements a simple school roster system."""

class School:
    """The School class manages students and their grades."""
    def __init__(self):
        self.school = {}
        self.add = []
        self.all_students = set()  # Set to track all student names for efficient lookup

    def add_student(self, name: str, grade: int) -> None:
        """Add a student to the school roster.
        
        :param name: The student's name
        :type name: str
        :param grade: The student's grade
        :type grade: int
        :returns: None
        """
        if name in self.all_students:
            self.add.append(False)
        else:
            students = self.school.setdefault(grade, [])
            students.append(name) # Add the student to the list for the grade
            self.all_students.add(name)  # Add to the set
            self.add.append(True)

    def added(self):
        """Track which students were successfully added."""
        return self.add

    def roster(self) -> list:
        """List all the students in the school in order."""
        # Get the grades in sorted order
        sorted_grades = sorted(self.school.keys())

        # Collect students from each grade in sorted order, flattening the resulting list
        students_by_grade = []
        for grade in sorted_grades:
            sorted_students = sorted(self.school[grade])
            students_by_grade.extend(sorted_students)

        return students_by_grade

    def grade(self, grade_number: int) -> list:
        """Return a sorted list of students in this grade.
        
        :param grade_number: The grade number
        :type grade_number: int
        :returns: A sorted list of student names in the specified grade
        """
        return sorted(self.school.get(grade_number, []))

def main():
    """Main function to demonstrate the School class."""
    school = School()
    school.add_student(name="Blair", grade=3)
    school.add_student(name="James", grade=3)
    school.add_student(name="James", grade=5)
    school.add_student(name="Paul", grade=5)
    print(f"Students in grade 3: {school.grade(3)}")
    print(f"Students in grade 5: {school.grade(5)}")
    print(f"Addition results: {school.added()}")
    print(f"Full roster: {school.roster()}")

if __name__ == "__main__":
    main()
