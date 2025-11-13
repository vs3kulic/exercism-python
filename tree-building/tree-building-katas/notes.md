# Design Decisions: Class Methods vs Standalone Functions

## PhoneNumber: Methods within the Class

### Encapsulation
- The `PhoneNumber` class encapsulates all the logic related to processing, validating, and formatting phone numbers.
- All methods operate directly on the `PhoneNumber` instance's data (`self._cleaned_number`), so it makes sense to keep them inside the class.

### Single Responsibility
- The `PhoneNumber` class is responsible for everything related to phone numbers: cleaning, validating, and formatting.
- Keeping the methods inside the class ensures that all phone number logic is in one place.

### Object-Oriented Design
- A phone number is a self-contained object with attributes (e.g., `number`, `area_code`) and behaviors (e.g., `pretty()`).
- The methods are tightly coupled to the `PhoneNumber` instance, so they belong in the class.

## Tree Building: Separate Functions

### Separation of Concerns
- The `Record` and `Node` classes are data containers. They don't "know" how to validate or build trees; they just hold data.
- The tree-building logic is a separate concern and doesn't belong to the `Record` or `Node` classes.

### Reusability
- The helper functions (`_validate_records`, `_create_nodes`, etc.) are reusable and operate on lists of `Record` or `Node` objects.
- They don't need to be tied to a specific class, making them more flexible.

### Procedural Nature
- Tree-building is a process that involves multiple steps (validation, node creation, relationship establishment).
- It's easier to manage this process with standalone functions that work together, rather than embedding everything in a class.

### Avoid Overloading Classes
- If you put all the tree-building logic into the `Record` or `Node` classes, those classes would become bloated and take on too many responsibilities.
- Keeping the logic in separate functions ensures that the classes remain simple and focused on their primary role: holding data.

## Key Difference: Responsibility
- **PhoneNumber**: The class is responsible for everything related to phone numbers, so the methods belong inside the class.
- **Tree Building**: The `Record` and `Node` classes are not responsible for building the tree. They're just data containers, so the tree-building logic is kept separate.

## Could We Move Tree-Building Logic into a Class?
- Yes, but it would change the design:
  - You could create a `TreeBuilder` class to encapsulate the tree-building process.
  - However, this would add complexity without much benefit, as the current design is already clean and modular.

## Summary
- **PhoneNumber**: The class encapsulates all logic because it's tightly coupled to the phone number data.
- **Tree Building**: The logic is separate because the `Record` and `Node` classes are just data containers, and the tree-building process is a distinct responsibility.

## Notes about dataclasses

# Design Decisions: Class Methods vs Standalone Functions
...existing code...

## Notes about dataclasses

Dataclasses (stdlib, 3.7+) are a lightweight way to declare plain data holders. They reduce boilerplate and make intent explicit, keeping the focus on algorithmic logic. @dataclass auto-generates __init__, __repr__, and __eq__ (optionally ordering and hashing). Use field(default_factory=list) to avoid shared mutable defaults and __post_init__ for validation or derived fields. Prefer frozen=True for immutable records. Inspect metadata with dataclasses.fields() or the class attribute __dataclass_fields__ when building serializers or debug helpers. Avoid order=True when ordering semantics are unclear or fields are mutable; implement a custom __lt__ for single-key sorting. Use asdict()/astuple() for quick serialization. 