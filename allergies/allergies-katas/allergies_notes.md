# Bitwise Operations & Binary Conversion Notes

## Converting Decimal to Binary

### Example: Converting 509 to Binary
```
509 ÷ 2 = 254 remainder 1  (509 % 2 = 1)
254 ÷ 2 = 127 remainder 0  (254 % 2 = 0)
127 ÷ 2 = 63  remainder 1  (127 % 2 = 1)
63  ÷ 2 = 31  remainder 1  (63 % 2 = 1)
31  ÷ 2 = 15  remainder 1  (31 % 2 = 1)
15  ÷ 2 = 7   remainder 1  (15 % 2 = 1)
7   ÷ 2 = 3   remainder 1  (7 % 2 = 1)
3   ÷ 2 = 1   remainder 1  (3 % 2 = 1)
1   ÷ 2 = 0   remainder 1  (1 % 2 = 1)
```

**Result:** Reading remainders from bottom to top gives us `111111101`

## Binary Position System

```
Position: 87654321₀ (counting from 0, right to left)
Binary:   11111110₁
Values:   25612864321₁
```

- **LSB (Least Significant Bit):** Rightmost bit, smallest value (2⁰ = 1)
- **MSB (Most Significant Bit):** Leftmost bit, largest value

## Powers of 2 in Binary

Each power of 2 creates a binary number with exactly one bit set:

| Decimal | Power | Binary  |
|---------|-------|---------|
| 1       | 2⁰    | 1       |
| 2       | 2¹    | 10      |
| 4       | 2²    | 100     |
| 8       | 2³    | 1000    |
| 16      | 2⁴    | 10000   |

## Bitwise AND Operation - The Magic Explained

### Truth Table for AND
| Bit A | Bit B | A & B |
|-------|-------|-------|
| 0     | 0     | 0     |
| 0     | 1     | 0     |
| 1     | 0     | 0     |
| 1     | 1     | 1     |

**Rule:** Only `1 & 1 = 1`, everything else is `0`.

### How AND Works
The `&` operator compares each bit position. It returns `1` only if **both** bits are `1`:

```
  509: 111111101
&   2: 000000010
    -----------
       000000000 = 0
```

### The Mind-Blowing Part: Automatic Zero-Padding

When you do `509 & 2`, the computer treats them as:

```
509: 111111101  (9 bits)
  2: 000000010  (conceptually padded to 9 bits)
```

But `2` in its "natural" form is just `10` (2 bits). **The CPU automatically extends it:**

```
Original 2:  10
Padded 2:    000000010
```

### How the CPU Handles This

The CPU doesn't actually "pad" - it processes bit by bit, treating missing bits as `0`:

```
Position: 876543210
509:      111111101
2:        000000010  ← Leading zeros are implicit!
          ---------
Result:   000000000
```

### Position-by-Position Breakdown
- Position 0: `1 & 0 = 0` ← 2 has implicit 0 here
- Position 1: `0 & 1 = 0` ← The "peanuts" bit (value 2) - explicit 1
- Position 2: `1 & 0 = 0` ← 2 has implicit 0 here
- All other positions: `1 & 0 = 0` ← All implicit zeros

### The Bit Mask Concept

Each allergy value (power of 2) acts as a **bit mask**:

```
eggs (1):      000000001  ← Only position 0 is 1
peanuts (2):   000000010  ← Only position 1 is 1
shellfish (4): 000000100  ← Only position 2 is 1
```

When you do `score & allergy_value`, you're asking:
**"Is the specific bit for this allergy set in the score?"**

### Example: 509 & 1 (checking for eggs)

```
509: 111111101
  4: 000000100
    -----------
     000000100 = 1 (non-zero = allergic!)
```

### Why `== 1` Checks the LSB

The condition `== 1` checks the least significant bit (LSB) because the binary representation of `1` is `0001`. This means only the rightmost bit is set to `1`, and all other bits are `0`.

When performing a bitwise `AND` operation (`&`), the result will only be `1` if the binary representation of the two numbers has the least significant bit set to `1` in both numbers. Here's why:

1. **Bitwise `AND` Operation**:
   - The `&` operator compares each bit position.
   - If both bits at the same position are `1`, the result at that position is `1`.
   - Otherwise, the result at that position is `0`.

2. **Binary Representation of `1`**:
   - The binary representation of `1` is `0001`.
   - This means only the least significant bit (rightmost bit) is `1`.

3. **Effect of `== 1`**:
   - After the `&` operation, the result will only be `1` if the least significant bit of the two numbers is `1`.
   - For example:
     - `5 & 1`:
       - `5` in binary: `0101`
       - `1` in binary: `0001`
       - Result: `0001` (which is `1` in decimal).
     - `4 & 1`:
       - `4` in binary: `0100`
       - `1` in binary: `0001`
       - Result: `0000` (which is `0` in decimal).

In the context of the `allergic_to` function, the allergy values are powers of 2 (e.g., `1`, `2`, `4`, `8`), which correspond to individual bits in the binary representation. The `== 1` condition only checks if the least significant bit is set, which is not sufficient to determine allergies for other values.

### Why we check for `!= 0`

The condition `!= 0` is used to check if the result of a bitwise `AND` operation is non-zero. This is important because a non-zero result indicates that at least one bit is set to `1` in the positions where both operands have `1` bits. Here's why this works:

1. **Bitwise `AND` Operation**:
   - The `&` operator compares each bit position of two numbers.
   - If both bits at the same position are `1`, the result at that position is `1`.
   - Otherwise, the result at that position is `0`.

2. **Non-Zero Result**:
   - A non-zero result means that there is at least one position where both numbers have a `1` bit.
   - For example:
     - `5 & 2`:
       - `5` in binary: `0101`
       - `2` in binary: `0010`
       - Result: `0000` (which is `0` in decimal, so `!= 0` is `False`).
     - `5 & 1`:
       - `5` in binary: `0101`
       - `1` in binary: `0001`
       - Result: `0001` (which is `1` in decimal, so `!= 0` is `True`).

3. **Why Not `== 1`?**:
   - Using `== 1` would only check if the result is exactly `1`, which corresponds to the least significant bit being set.
   - However, allergy values are powers of 2 (e.g., `1`, `2`, `4`, `8`), and their binary representations have a single `1` bit in different positions. The result of `&` will match the allergy value, not necessarily `1`.

By using `!= 0`, we ensure that the function correctly identifies any non-zero result, which means the person is allergic to the given item.

## Why This is Brilliant

1. **Single Operation**: Check any allergy with one `&` operation
2. **Simultaneous Processing**: All bit positions evaluated at once
3. **Perfect Isolation**: Each allergy has its own unique bit
4. **Blazing Fast**: Bitwise operations are among the fastest CPU operations
5. **Compact Storage**: 8 allergies fit in a single byte!

**The `&` operator is like a spotlight that illuminates only the bit you care about!** 🔦

### Why Bitwise Operations Are Fast

- Bitwise operations are among the fastest operations a CPU can perform because they happen directly in the **Arithmetic Logic Unit (ALU)** without any abstraction layers. 
- Unlike arithmetic operations that might require multiple clock cycles, carry propagation, or floating-point calculations, bitwise operations work on all bits **simultaneously in parallel circuits**. Each bit position is processed by dedicated transistors at the same time - there's no sequential processing, no memory lookups, no function calls, and no interpreter overhead. 
- The CPU literally just applies voltage patterns to logic gates and gets an instant result. It's as close to the metal as you can get - pure electrical switches flipping in nanoseconds, it's literally the speed of electricity flowing through silicon.

### Notes about the ALU

The **ALU (Arithmetic Logic Unit)** is inside the **CPU chip**. It's a **dedicated section of transistors** etched directly onto the silicon die of your processor - not software, but actual **microscopic electrical circuits**.

#### Physical Location
```
Your Computer
├── Motherboard
    ├── CPU Socket
        ├── CPU Chip (silicon die)
            ├── Control Unit
            ├── Registers  
            ├── Cache Memory
           
**Important:** Bitwise operations happen **simultaneously** on all positions, not sequentially.

## Exercise Design

The Exercise is Designed for Bitwise Operations. 

- Powers of 2: Each allergy value is deliberately a power of 2
    - eggs: 1, peanuts: 2, shellfish: 4, etc.
    - This ensures each allergy gets its own unique bit position

- Additive Scoring: The total score is the sum of all allergies
    - If allergic to eggs (1) + peanuts (2) = score of 3
    - In binary: 1 + 10 = 11 (bits 0 and 1 are set)

- No Overlap: Powers of 2 guarantee no conflicts
    - Each allergy "owns" exactly one bit position
    - No two allergies can interfere with each other

### Use-cases for Bitwise Operations

- Flags and permissions (read: 4, write: 2, execute: 1)
- Game states (alive, invincible, frozen, etc.)
- Feature toggles in software
- Hardware registers and embedded programming

### Bitwise Operations

- File permissions in Unix (rwx = 111 = 7)
- Network masks and IP addresses
- Graphics programming (RGB colors, alpha channels)
- Game development (collision detection, state flags)
- Embedded systems and IoT devices

### Summary of Binary Operators

| Operator | Name           | Example   | Result |
|----------|----------------|-----------|--------|
| `&`      | AND            | `5 & 3`  | `1`    |
| `|`      | OR             | `5 | 3`  | `7`    |
| `^`      | XOR            | `5 ^ 3`  | `6`    |
| `~`      | NOT (Unary)    | `~5`     | `-6`   |
| `<<`     | Left Shift     | `5 << 1` | `10`   |
| `>>`     | Right Shift    | `5 >> 1` | `2`    |
