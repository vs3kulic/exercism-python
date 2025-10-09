### Comparison of Two Implementations

#### 1. Direction Representation
- **Current Implementation**: Uses a list (`DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]`) and represents directions as integer indices (`0` for "NORTH", `1` for "EAST", etc.). The `direction_string` property converts the index back to a string.
- **Alternative Implementation**: Uses strings directly (e.g., `NORTH`, `EAST`, etc.) and relies on dictionaries (`DIRECTIONS_LEFT` and `DIRECTIONS_RIGHT`) for turning logic.

#### 2. Turning Logic
- **Current Implementation**: Uses modular arithmetic to calculate the new direction index:
  ```python
  self.direction = (self.direction + step) % len(DIRECTIONS)
  ```
  - `step = 1` for right turns, `step = -1` for left turns.
- **Alternative Implementation**: Uses dictionaries to map the current direction to the new direction:
  ```python
  self.direction = direction_mapping[self.direction]
  ```

#### 3. Movement Logic
- Both implementations use `DIRECTION_DELTAS` to map directions to coordinate changes:
  ```python
  dx, dy = DIRECTION_DELTAS[self.direction]
  self.coordinates = (x + dx, y + dy)
  ```

#### 4. Readability
- **Current Implementation**: Compact and efficient, but requires the `direction_string` property for human-readable output.
- **Alternative Implementation**: More explicit and intuitive, but verbose due to the use of multiple dictionaries.

#### 5. Extensibility
- **Current Implementation**: Adding new directions requires updating the `DIRECTIONS` list and `DIRECTION_DELTAS`.
- **Alternative Implementation**: Adding new directions requires updating `DIRECTIONS_LEFT`, `DIRECTIONS_RIGHT`, and `DIRECTION_DELTAS`.

#### 6. Performance
- **Current Implementation**: Faster due to integer arithmetic for turning.
- **Alternative Implementation**: Slightly slower due to dictionary lookups.

#### 7. Code Complexity
- **Current Implementation**: Less complex, as modular arithmetic handles turning efficiently.
- **Alternative Implementation**: More complex, as turning logic relies on multiple dictionaries.

### Summary Table
| Feature                | Current Implementation               | Alternative Implementation             |
|------------------------|---------------------------------------|-----------------------------------------|
| **Direction Storage**  | List with indices                   | Strings with dictionaries              |
| **Turning Logic**      | Modular arithmetic                  | Dictionaries                           |
| **Movement Logic**     | Same (`DIRECTION_DELTAS`)           | Same (`DIRECTION_DELTAS`)              |
| **Readability**        | Compact and efficient               | Explicit but verbose                   |
| **Extensibility**      | Easy to add directions              | Requires updating multiple dictionaries|
| **Performance**        | Faster (integer arithmetic)         | Slightly slower (dictionary lookups)   |
| **Complexity**         | Less complex                        | More complex                           |

### Explanation of Modular Arithmetic in `_turn`

The `_turn` method uses modular arithmetic to calculate the new direction when the robot turns. This ensures that the direction index wraps around correctly when it goes out of bounds.

#### Formula Used:
```python
self.direction = (self.direction + step) % len(DIRECTIONS)
```
- `self.direction`: The current direction of the robot, represented as an index in the `DIRECTIONS` list.
- `step`: The direction of the turn (`+1` for right, `-1` for left).
- `len(DIRECTIONS)`: The total number of directions (4 in this case).

#### Why Modular Arithmetic?
1. **Wrap-Around Behavior**:
   - Modular arithmetic ensures that the index wraps around when it goes out of bounds.
   - Example:
     - Turning right from "WEST" wraps back to "NORTH".
     - Turning left from "NORTH" wraps to "WEST".

2. **Efficiency**:
   - Modular arithmetic is a simple and efficient way to handle circular lists like `DIRECTIONS`.

3. **Compact Code**:
   - The logic is implemented in a single line, avoiding verbose conditionals or additional checks.

#### Example Calculations:
1. **Right Turn**:
   - Initial State: `self.direction = 0` (facing "NORTH")
   - `step = 1` (right turn)
   - Calculation:
     ```python
     self.direction = (0 + 1) % 4
     self.direction = 1
     ```
   - Result: `self.direction = 1` (facing "EAST")

2. **Left Turn**:
   - Initial State: `self.direction = 0` (facing "NORTH")
   - `step = -1` (left turn)
   - Calculation:
     ```python
     self.direction = (0 - 1) % 4
     self.direction = -1 % 4
     self.direction = 3
     ```
   - Result: `self.direction = 3` (facing "WEST")

3. **Multiple Right Turns**:
   - Initial State: `self.direction = 2` (facing "SOUTH")
   - `step = 1` (right turn)
   - Calculation:
     ```python
     self.direction = (2 + 1) % 4
     self.direction = 3
     ```
   - Result: `self.direction = 3` (facing "WEST")

   - Another Right Turn:
     ```python
     self.direction = (3 + 1) % 4
     self.direction = 0
     ```
   - Result: `self.direction = 0` (facing "NORTH")

4. **Multiple Left Turns**:
   - Initial State: `self.direction = 1` (facing "EAST")
   - `step = -1` (left turn)
   - Calculation:
     ```python
     self.direction = (1 - 1) % 4
     self.direction = 0
     ```
   - Result: `self.direction = 0` (facing "NORTH")

   - Another Left Turn:
     ```python
     self.direction = (0 - 1) % 4
     self.direction = -1 % 4
     self.direction = 3
     ```
   - Result: `self.direction = 3` (facing "WEST")

#### Key Takeaway:
- Modular arithmetic ensures that the direction index wraps around correctly, making the `_turn` method compact and efficient.

### Why Does `-1 % 4 == 3`?

#### Step-by-Step Explanation
1. **Formula for Modulo in Python**:
   Python's `%` operator ensures that the result is **non-negative** when the divisor (in this case, `4`) is positive. The formula Python uses is:
   ```
   result = dividend - (divisor * floor(dividend / divisor))
   ```
   Here:
   - **Dividend**: `-1`
   - **Divisor**: `4`

2. **Perform Integer Division (`//`)**:
   Calculate the **floor division** of `-1 / 4`:
   ```
   floor(-1 / 4) = -1
   ```
   - Python uses **floor division**, which rounds **down** to the nearest integer. Since `-1 / 4 = -0.25`, the floor is `-1`.

3. **Multiply the Divisor by the Floor Division Result**:
   Multiply the divisor (`4`) by the result of the floor division (`-1`):
   ```
   4 * -1 = -4
   ```

4. **Subtract**:
   Subtract this value from the dividend (`-1`):
   ```
   -1 - (-4) = -1 + 4 = 3
   ```

5. **Final Result**:
   ```
   -1 % 4 = 3
   ```

#### Why Does This Work?
- The modulo operation in Python ensures that the result is **non-negative** when the divisor is positive.
- In this case, `-1` wraps around to the equivalent positive remainder when divided by `4`.

#### Visualizing the Wrap-Around
Think of the `DIRECTIONS` list as a circular array:
```python
DIRECTIONS = ["NORTH", "EAST", "SOUTH", "WEST"]
```

The indices are:
```
  0 → "NORTH"
  1 → "EAST"
  2 → "SOUTH"
  3 → "WEST"
```

If you move **backward** from index `0` (e.g., `-1`), you "wrap around" to the last index (`3`):
```
-1 → 3
```

#### Key Takeaway
In Python:
- The `%` operator ensures the result is **non-negative** when the divisor is positive.
- `-1 % 4 = 3` because `-1` wraps around to the last valid index in a circular list of size `4`.

### Recommendation
- Use the **current implementation** for compactness, efficiency, and scalability.
- Use the **robot_simulator_dicts** if you prefer explicit logic and find dictionaries more intuitive.

