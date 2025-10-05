"""This module implements a Matrix class."""

class Matrix:
    """A class to represent a mathematical matrix."""
    def __init__(self, matrix_string: str):
        self.matrix_string = matrix_string

    def parse_matrix(self) -> list[list[int]]:
        """Parse the matrix string into a 2D list of integers."""
        rows = self.matrix_string.split("\n")
        matrix = []
        for row in rows:
            mapped = map(int, row.split()) # Without split(), the row string would be passed as a single argument to int, which would raise an error because int cannot directly parse a space-separated string like "1 2 3".
            converted = list(mapped)
            matrix.append(converted)
        return matrix

    def row(self, index: int) -> list[int]:
        """Return the row at the given 1-based index.
        
        :param index: 1-based row index
        :type index: int
        :return: list of integers in the specified row
        :rtype: list[int]
        """
        matrix = self.parse_matrix()
        row = matrix[index - 1]
        return row

    def column(self, index: int) -> list[int]:
        """Return the column at the given 1-based index.
        
        :param index: 1-based column index
        :type index: int
        :return: list of integers in the specified column
        :rtype: list[int]
        """
        matrix = self.parse_matrix()
        column = [row[index-1] for row in matrix]
        return column

def main():
    """Main function to demonstrate the Matrix class."""
    matrix_string = "1 2 3\n4 5 6\n7 8 9"
    matrix = Matrix(matrix_string)
    print("Matrix:")
    print(matrix.parse_matrix())
    print("Row 2:", matrix.row(2))
    print("Column 3:", matrix.column(3))

if __name__ == "__main__":
    main()
