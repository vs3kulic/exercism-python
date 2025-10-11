"""This module implements a simple school roster system."""

class School:
    """The School class manages students and their grades."""
    def __init__(self):
        self.school = {}
        self.add = []

    def add_student(self, name: str, grade: int) -> None:
        """Add a student to the school roster.
        
        :param name: The student's name
        :type name: str
        :param grade: The student's grade
        :type grade: int
        :returns: None
        """
        if name not in self.roster():
            self.school[grade] = self.school.get(grade, []) + [name]
            self.add.append(True)
        else:
            self.add.append(False)

    def added(self):
        """Track which students were successfully added."""
        return self.add
    
    def roster(self) -> list:
        """List all the students in the school in order."""
        # Get the grades in sorted order
        sorted_grades = sorted(self.school.keys())

        # Collect students from each grade in sorted order
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
    school.add_student(name="Harry", grade=3)
    school.add_student(name="Ron", grade=3)
    school.add_student(name="Ron", grade=5)
    school.add_student(name="Draco", grade=5)
    print(f"Students in grade 3: {school.grade(3)}")
    print(f"Students in grade 5: {school.grade(5)}")
    print(f"Full roster: {school.roster()}")
    print(f"Addition results: {school.added()}")

if __name__ == "__main__":
    main()
