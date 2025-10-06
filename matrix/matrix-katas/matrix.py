"""This module implements a Matrix class."""

class Matrix:
    """A class to represent a mathematical matrix."""
    def __init__(self, matrix_string: str):
        self.matrix = [
            [int(i) for i in row.split()]
            for row in matrix_string.split("\n")
        ]

    def row(self, index: int) -> list[int]:
        """Return the row at the given 1-based index.
        
        :param index: 1-based row index
        :type index: int
        :return: list of integers in the specified row
        :rtype: list[int]
        """
        row = self.matrix[index-1]
        return row

    def column(self, index: int) -> list[int]:
        """Return the column at the given 1-based index.
        
        :param index: 1-based column index
        :type index: int
        :return: list of integers in the specified column
        :rtype: list[int]
        """
        column = [row[index-1] for row in self.matrix]
        return column

def main():
    """Main function to demonstrate the Matrix class."""
    matrix_string = "1 2 3\n4 5 6\n7 8 9"
    matrix = Matrix(matrix_string)
    print("Matrix:")
    print("Row 2:", matrix.row(2))
    print("Column 2:", matrix.column(2))

if __name__ == "__main__":
    main()
