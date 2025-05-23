```markdown
# Transposing Wagon Rows in Python

This example demonstrates how to transpose a list of wagon rows to analyze trains by wagon position rather than by train.

## Original Data

Each train is a list of wagons, where each wagon is represented as a tuple `(wagon number, color)`:

```
wagons_rows = [
    [(1, 'red'),   (2, 'blue'),  (3, 'green')],   # Train 1
    [(4, 'red'),   (5, 'blue'),  (6, 'green')],   # Train 2
    [(7, 'red'),   (8, 'blue'),  (9, 'green')]    # Train 3
]
```

## Transposing the Data

To group all wagons by their position across trains, use the following code:

```
transposed = [list(row) for row in zip(*wagons_rows)]
# transposed is all first wagons, transposed is all second wagons, etc.
```

The result:

```
transposed = [
    [(1, 'red'), (4, 'red'), (7, 'red')],    # All first-position wagons
    [(2, 'blue'), (5, 'blue'), (8, 'blue')], # All second-position wagons
    [(3, 'green'), (6, 'green'), (9, 'green')] # All third-position wagons
]
```

## Analyzing by Wagon Position

Now, you can easily check if all wagons in each position across trains have the same color:

```
for idx, position in enumerate(transposed, start=1):
    colors = {wagon for wagon in position}
    if len(colors) == 1:
        print(f"All wagons in position {idx} are {colors.pop()}.")
    else:
        print(f"Wagons in position {idx} have different colors: {colors}")
```

**Output:**
```
All wagons in position 1 are red.
All wagons in position 2 are blue.
All wagons in position 3 are green.
```

## Why Transpose?

Transposing lets you analyze your trains **vertically** (by wagon position across trains), not just **horizontally** (by train). This is super handy for comparisons, consistency checks, and many other real-world tasks!
```