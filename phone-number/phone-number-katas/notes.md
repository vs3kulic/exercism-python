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