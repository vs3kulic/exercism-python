"""This module implements a simple school roster system."""

class School(object):
    """The School class manages students and their grades."""
    def __init__(self):
        """Initialize a School object."""
        self.grades = {} # dict key=grade, value=list of names
        self.result = []

    def add_student(self, name: str, grade: int) -> bool:
        """Tries to add a student to the school roster.
        
        :param name: The student's name
        :type name: str
        :param grade: The student's grade
        :type grade: int
        :returns: True if the student was added, False if they were already enrolled
        """
        # Check if the student is already in the school (any grade)
        if any(name in students for students in self.grades.values()):
            self.result.append(False)
            return False

        # Add the student to the specified grade
        self.grades.setdefault(grade, []).append(name) # check if grade exists, if not create it and set to empty list, then append name
        self.result.append(True)
        return True

    def grade(self, num: int) -> list:
        """Return a sorted list of students in this grade.
        
        :param num: The grade number
        :type num: int
        :returns: A sorted list of student names in the specified grade
        """
        students_in_grade = self.grades.get(num, []) # get list of students in the grade, or empty list if grade doesn't exist
        return sorted(students_in_grade)

    def roster(self) -> list:
        """List all the students in the school in order."""
        # Get the grades in sorted order
        sorted_grades = sorted(self.grades.keys())

        # Collect students from each grade in sorted order
        students_by_grade = []
        for grade in sorted_grades:
            students_by_grade.append(self.grade(grade))

        # Flatten the list of lists into a single list
        all_students = []
        for grade_students in students_by_grade:
            all_students.extend(grade_students)

        return all_students

    def added(self):
        """Track which students were successfully added."""
        return self.result

def main():
    """Main function to demonstrate the School class."""
    school = School("Hogwarts")
    school.add_student(name="Harry", grade=5)
    school.add_student(name="Hermione", grade=5)
    school.add_student(name="Ron", grade=5)
    school.add_student(name="Draco", grade=5)
    print(f"Students in grade 5: {school.grade(5)}")
    print(f"Full roster: {school.roster()}")
    print(f"Addition results: {school.added()}")

if __name__ == "__main__":
    main()
