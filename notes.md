# Checking Available Methods on Objects in Python

## Using `dir()`
The `dir()` function returns a list of all attributes and methods available on an object.

```python
digits = [1, 2, 3, 4, 5]
print(dir(digits))
# Output: ['__add__', '__class__', '__contains__', ..., 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

## Filtering Only Methods
To see only callable methods (excluding attributes):

```python
digits = [1, 2, 3, 4, 5]
methods = [method for method in dir(digits) if callable(getattr(digits, method))]
print(methods)
# Output: ['__add__', '__class__', '__contains__', ..., 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

## Using `help()`
Get detailed documentation for an object and its methods:

```python
digits = [1, 2, 3, 4, 5]
help(digits)
# Shows detailed help for list object and all its methods
```

## Checking if a Specific Method Exists
Use `hasattr()` to check if an object has a particular attribute or method:

```python
digits = [1, 2, 3, 4, 5]
print(hasattr(digits, 'reverse'))  # True
print(hasattr(digits, 'nonexistent'))  # False
```

## Interactive Exploration
In VS Code or IPython:
- Type the object name followed by a dot: `digits.`
- Press Tab for autocomplete suggestions showing available methods

## Common List Methods (Example)
For a list object, common methods include:
- `append(item)` - Add to end
- `extend(iterable)` - Add multiple items
- `insert(index, item)` - Insert at position
- `remove(item)` - Remove first occurrence
- `pop(index)` - Remove and return item
- `clear()` - Remove all items
- `index(item)` - Find index
- `count(item)` - Count occurrences
- `sort()` - Sort in place
- `reverse()` - Reverse in place
- `copy()` - Shallow copy

## Pro Tips
- `dir()` - Quick overview of all attributes/methods
- `help()` - Detailed documentation
- VS Code IntelliSense - Type `object.` and see suggestions
- Python docs online - Comprehensive reference