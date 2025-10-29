# Distinction Between Attributes and Properties in Python

## Attributes
- **Definition**: Attributes are variables that belong to an object or class.
- **Direct Access**: Accessed directly without any additional logic.
- **Use Case**: Used when no additional processing is required for getting or setting a value.
- **Example**:
  ```python
  class Example:
      def __init__(self):
          self.attribute = 42

  obj = Example()
  print(obj.attribute)  # Direct access
  ```

## Properties
- **Definition**: Properties are methods that are accessed like attributes.
- **Encapsulation**: Allow additional logic to be executed when getting, setting, or deleting a value.
- **Use Case**: Used when you need to control access to an attribute or add validation logic.
- **Example**:
  ```python
  class Example:
      def __init__(self):
          self._attribute = 42

      @property
      def attribute(self):
          return self._attribute

      @attribute.setter
      def attribute(self, value):
          if value < 0:
              raise ValueError("Value must be non-negative")
          self._attribute = value

  obj = Example()
  print(obj.attribute)  # Access via getter
  obj.attribute = 10    # Access via setter
  ```

## Key Differences
| Aspect              | Attributes                          | Properties                          |
|---------------------|-------------------------------------|-------------------------------------|
| **Definition**      | Variables of an object or class    | Methods accessed like attributes    |
| **Logic**           | No additional logic                | Can include logic (e.g., validation)|
| **Access**          | Direct                             | Controlled via getter/setter        |
| **Use Case**        | Simple data storage                | Encapsulation and validation        |

---

## What is an Invariant?

- **Definition**: An invariant is a condition or rule that remains true throughout the lifetime of an object or during the execution of a program. It ensures that the object is always in a valid and consistent state.

- **Why It Matters**:
  - Invariants help maintain **data integrity** by ensuring that the internal state of an object is always valid.
  - They make the code **easier to reason about** because you can trust that certain conditions are always true.
  - They prevent **bugs** by enforcing rules that cannot be violated.

- **Example in the `PhoneNumber` Class**:
  - The invariant is that `_cleaned_number` always contains a valid, cleaned phone number.
  - Once the validation pipeline in `__init__` completes, `_cleaned_number` is guaranteed to:
    1. Contain only digits.
    2. Be exactly 10 digits long.
    3. Have valid area and exchange codes.
  - This means that any method (like `number`, `area_code`, or `pretty`) can safely use `_cleaned_number` without needing to revalidate it.

- **Key Takeaway**:
  - Invariants ensure that objects are always in a **valid state**, making your code more reliable and easier to maintain.

---

## How the `PhoneNumber` Class Assigns State

- `__init__` runs a **validation pipeline** on the raw input string:
  1. `_validate_characters(number)` → ensures every character is a digit or one of the allowed separators (`()+-. `). Letters or disallowed punctuation raise immediately.
  2. `_extract_and_clean_digits(number)` → combines digit extraction and cleaning:
     - Strips everything down to the raw digits.
     - Removes the leading `1` if the number has 11 digits.
  3. `_validate_raw_length(cleaned_number)` → enforces 10 digits, or 11 digits that begin with the country code `1`.
  4. `_validate_codes(cleaned_number)` → checks the area and exchange rules on the cleaned string.

- Only after all stages pass does the class store data:  
  `self._cleaned_number = ...` — this is the single source of truth.

- Read-only API:
  - `number` (property) returns `self._cleaned_number`.
  - `area_code` (property) slices the first three digits.
  - `pretty()` formats the stored digits as `(NXX)-NXX-XXXX`.

Because the class never reprocesses the raw string after `__init__`, every consumer reads from the validated `_cleaned_number`, keeping the invariant intact.

---

## Why the Initializer Stores Data

- **Purpose**: The initializer (`__init__`) ensures that the object is fully validated and in a consistent state before it is used.
- **What is Stored**:
  - `_cleaned_number`: The validated and cleaned phone number, which is the single source of truth for the object.
- **Why It Matters**:
  - Storing `_cleaned_number` ensures that all methods and properties operate on consistent, validated data.
  - This avoids redundant processing and guarantees that the object is always in a valid state.

---

## Is `pretty` a Static Method?

- **No, `pretty` is not a static method.** It is an **instance method** because it relies on the instance attribute `_cleaned_number` to format the phone number.

### Why `pretty` is an Instance Method:
1. **Instance Dependency**:
   - The `pretty` method uses `self._cleaned_number`, which is specific to the instance of the `PhoneNumber` class.
   - Each instance of `PhoneNumber` could have a different `_cleaned_number`, so the method needs to operate in the context of the instance.

2. **Encapsulation**:
   - The `pretty` method is part of the `PhoneNumber` class and operates on the internal state of the object, encapsulating the logic for formatting the phone number.

3. **Cleaner API**:
   - As an instance method, you can call `phone.pretty()` directly, which is more intuitive than passing the cleaned number explicitly.

### What Would a Static Method Look Like?
If `pretty` were a static method, it would not use `self` and would require the cleaned number to be passed as an argument:
```python
@staticmethod
def pretty(cleaned_number: str) -> str:
    """Return the phone number in pretty format: (NXX) NXX-XXXX."""
    area_code = cleaned_number[:3]
    exchange_code = cleaned_number[3:6]
    subscriber_number = cleaned_number[6:]
    return f"({area_code})-{exchange_code}-{subscriber_number}"
```

You would call it like this:
```python
phone = PhoneNumber("(223) 456-7890")
print(PhoneNumber.pretty(phone.number))  # Static method call
```

### Why Keep It as an Instance Method?
- **Encapsulation**: The `pretty` method operates on the internal state of the object (`_cleaned_number`), which aligns with object-oriented design principles.
- **Readability**: Using `phone.pretty()` is cleaner and more intuitive than calling a static method and passing the cleaned number explicitly.

### Key Takeaway:
The `pretty` method is an **instance method** because it depends on the instance attribute `_cleaned_number`. This design keeps the API clean and encapsulates the logic within the object.

