# Multidimensional Lists - From First Principles 🧠

## Start Simple: 1D Lists (What You Already Know) 📦

Think of a 1D list like a **row of boxes**:

```python
my_list = [10, 20, 30, 40, 50]
#          ↑   ↑   ↑   ↑   ↑
#          0   1   2   3   4  ← positions
```

**Access with ONE number:**
```python
my_list[0]  # Gets 10
my_list[2]  # Gets 30
my_list[4]  # Gets 50
```

**Easy! One box, one address!**

---

## 2D Lists: Think "Boxes Inside Boxes" 📦📦

### Visual: Like a Grid or Table
```python
# Like a tic-tac-toe board:
grid = [
    [1, 2, 3],    # Row 0
    [4, 5, 6],    # Row 1  
    [7, 8, 9]     # Row 2
]
```

### Grid Layout:
```
    Col 0  Col 1  Col 2
Row 0  1     2     3
Row 1  4     5     6
Row 2  7     8     9
```

### Access with TWO numbers:
```python
grid[1][2]  # Row 1, Column 2 → Gets 6
#    ↑  ↑
#   row col

grid[0][0]  # Row 0, Column 0 → Gets 1
grid[2][1]  # Row 2, Column 1 → Gets 8
```

---

## Think Two Steps: 📍

### Step 1: Get the ROW (which is a list)
```python
grid = [
    [1, 2, 3],    # ← This whole thing is grid[0]
    [4, 5, 6],    # ← This whole thing is grid[1]
    [7, 8, 9]     # ← This whole thing is grid[2]
]

first_row = grid[0]  # first_row = [1, 2, 3]
```

### Step 2: Get the ITEM from that row
```python
first_row = grid[0]     # [1, 2, 3]
item = first_row[1]     # Gets 2

# Same as:
item = grid[0][1]       # Gets 2
```

---

## Real-World Examples 🌍

### Example 1: Grade Book
```python
# Each student has grades for different subjects
grades = [
    [85, 92, 78],  # Student 0: Math, English, Science
    [90, 88, 95],  # Student 1: Math, English, Science
    [76, 84, 82]   # Student 2: Math, English, Science
]

# Get Student 1's English grade:
english_grade = grades[1][1]  # Gets 88
#                      ↑  ↑
#                 student subject
```

### Example 2: Game Board
```python
# Checkers board (simplified 3x3)
board = [
    ['R', ' ', 'R'],  # Red pieces and empty spaces
    [' ', 'B', ' '],  # Black piece in middle
    ['B', ' ', 'B']   # Black pieces
]

# Check what's at position (1, 1):
center_piece = board[1][1]  # Gets 'B'
```

---

## Building 2D Lists 🏗️

### Method 1: Build row by row
```python
# Start empty
grid = []

# Add first row
grid.append([1, 2, 3])
# grid = [[1, 2, 3]]

# Add second row  
grid.append([4, 5, 6])
# grid = [[1, 2, 3], [4, 5, 6]]

# Add third row
grid.append([7, 8, 9])
# grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Method 2: Create all at once
```python
grid = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]
```

---

## Common Mistakes ❌

### Wrong: Thinking flat
```python
# This is NOT 2D - it's still 1D:
grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Just a long list!
```

### Right: Thinking nested
```python
# This IS 2D - lists inside a list:
grid = [
    [1, 2, 3],  # First row (a list)
    [4, 5, 6],  # Second row (a list)
    [7, 8, 9]   # Third row (a list)
]
```

---

## Practice Exercise 💪

Create this 2x2 grid:
```
  A  B
  C  D
```

**Solution:**
```python
grid = [
    ['A', 'B'],  # Row 0
    ['C', 'D']   # Row 1
]

# Test your understanding:
print(grid[0][0])  # Should print 'A'
print(grid[0][1])  # Should print 'B'  
print(grid[1][0])  # Should print 'C'
print(grid[1][1])  # Should print 'D'
```

---

## Your DP Table is Actually Easy! 🎯

**Good news: Your DP table is just 1D!**

```python
# Your DP table:
dp = [0, 1, 2, 1, 1, 2, 2]
#     0  1  2  3  4  5  6  ← positions (amounts)

# Simple access: dp[amount] = minimum_coins
# No second dimension needed!
```

---

## Key Insight 💡

**2D lists are just "a list of lists"**
- The outer list contains rows
- Each row is itself a list  
- You need two coordinates: [row][column]

**Think: Spreadsheet cells, game boards, or tables!**

---

## Quick Mental Check ✅

```python
# 1D (simple):
scores = [85, 90, 76, 88]
print(scores[2])  # Gets 76

# 2D (nested):
classroom = [
    [85, 90],  # Student 0's two grades
    [76, 88]   # Student 1's two grades  
]
print(classroom[1][0])  # Gets 76 (Student 1's first grade)
```

**Remember: [outer][inner] = [row][column] = [which_list][which_item_in_that_list]**