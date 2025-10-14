"""This file contains the solution approach for the Grade School exercise."""

# -----------------------
# REQUIREMENT
# -----------------------

# Given students' names along with the grade they are in,
# create a roster for the school.

# -----------------------
# METHODS
# -----------------------

# Add a student's name to the roster for a grade.
# Get a list of all students enrolled in a grade.
# Get a sorted list of all students in all grades.
#   - Grades should be sorted in ascending order (as 1, 2, 3, etc.).
#   - Students within a grade should be sorted alphabetically by name.

# -----------------------
# CONSTRAINTS
# -----------------------

# The tests expect the school roster to be implemented via a School `class`.
# All students only have one name.
# Each student cannot be added more than once to a grade or the roster.

# -----------------------
# SOLUTION APPROACH
# -----------------------

# The attributes of the `School` class should include:
#   - a list or dictionary to store students and their grades
#   - a list to track the results of adding students

# The School should have the following methods:
#   - `add_student()` to add a student to the roster
#   - `grade()` to get a list of students in a specific grade
#   - `roster()` to get a sorted list of all students in all grades
#   - `added()` to track which students were successfully added

# -----------------------
# NOTE ON DATA STRUCTURES
# -----------------------

# To efficiently manage the roster, we can use different data structures:
#   - we can save them as (name, grade) tuples in a list
#   - we can also use a dictionary with grades as keys and lists of names as values

# To decide which data structure to use, we can consider the operations we need to perform:
#   - Adding a student: both structures allow efficient addition.
#   - Retrieving students by grade: a dictionary allows direct access to the list of names
#     for a specific grade, making it more efficient than searching through a list of tuples.
#   - Getting a sorted list of all students: both structures can be sorted, but a
#     dictionary requires additional steps to sort the grades and then the names within each grade.

# -----------------------
# NOTE ON SORTING
# -----------------------

# If we decide to use a list of tuples, we can use the `bisect` module to maintain a sorted list.
# To add a student, we can use `bisect.insort()` to insert the (grade, name) tuple.
# In this case, bisect.insort() will:
#   - Compare the first element of the tuple (the grade) to determine the insertion point.
#   - Insert the tuple in the correct position to maintain the list sorted by grade in ascending order.
#   - If two tuples have the same grade, it will then compare the second element (the name)
#     to ensure the list remains sorted alphabetically within the same grade.
# Before we add a student, we should check if the student is already in the list to avoid duplicates.
#   - We can use a GENERATOR EXPRESSION to iterate through the list and check if any name matches the one we want to add.
#   - Other options include using a set to track names for O(1) average time complexity on lookups,
#     but this would require additional space and complexity to keep the set in sync with the list
#     of tuples.
#   - We can also use a list comprehension to create a list of names and check if the name is in that list,
#     but this would be less efficient than a generator expression as it creates an intermediate list.
# If we decide to use a dictionary, we can:
#   - Use the `setdefault()` method to initialize a list for a grade if it doesn't exist.
#   - Append the student's name to the list for that grade.
#   - Before adding, we can check if the name is already in any of the lists
#     using a generator expression to avoid duplicates.
#   - To get a sorted list of all students, we can:
#     - Sort the dictionary keys (grades) and then sort the names within each grade.
#     - Use a list comprehension to flatten the sorted lists of names into a single list.
#   - This approach is efficient for retrieving students by grade and allows for easy maintenance of the
#     roster.
#   - However, it requires more steps to get a fully sorted list of all students compared to a single sorted list of tuples.
# Overall, the choice between a list of tuples and a dictionary depends on the specific requirements
# and operations we need to perform most frequently.
