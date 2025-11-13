"""This module contains a function to build a tree from a list of records."""
from __future__ import annotations
from dataclasses import dataclass, field, fields, MISSING


@dataclass
class Record:
    """Class representing a record with an ID and a parent ID."""
    record_id: int
    parent_id: int

    def __lt__(self, other: Record) -> bool:
        """Compare two Record instances based on their record_id."""
        return self.record_id < other.record_id


@dataclass
class Node:
    """Class representing tree node with a node ID and children."""
    node_id: int
    children: list[Node] = field(default_factory=list)


def _validate_records(sorted_records: list[Record]) -> None:
    """Validate the integrity of the records.

    :param sorted_records: Sorted list of Record instances
    :type sorted_records: list[Record]
    :raises ValueError: If records do not form a valid tree structure
    """
    # First record must be root (record_id 0)
    if sorted_records[0].record_id != 0:
        raise ValueError("Record id is invalid or out of order.")

    # Last list element (zero-indexed) must match len to ensure continuity
    if sorted_records[-1].record_id != len(sorted_records) - 1:
        raise ValueError("Record id is invalid or out of order.")

    # Parent-child relationship rules
    if any(r.record_id < r.parent_id for r in sorted_records):
        raise ValueError("Node parent_id should be smaller than its record_id.")

    if any(
        r.record_id == r.parent_id and r.record_id != 0
        for r in sorted_records
    ):
        raise ValueError("Only root should have equal record and parent id.")


def _establish_relationships(sorted_records: list[Record]) -> list[Node]:
    """Create Node instances for each record and establish parent-child links.

    This helper returns the created list of nodes so callers can access the
    root. It combines node creation and linking into a single helper.

    :param sorted_records: List of sorted Record instances
    :type sorted_records: list[Record]
    :returns: List of Node instances with children linked
    :rtype: list[Node]
    """
    # Create all nodes
    nodes = [Node(record.record_id) for record in sorted_records]

    # Establish parent-child relationships, skipping the root
    for record in sorted_records[1:]:
        parent_node = nodes[record.parent_id]  # Get parent Node
        child_node = nodes[record.record_id]  # Get child Node
        parent_node.children.append(child_node)

    return nodes


def BuildTree(records: list[Record]) -> Node | None:
    """Build a tree structure from a list of records.

    :param records: List of Record instances
    :type records: list[Record]
    :returns: Root node of the built tree
    :rtype: Node (or None)
    """
    # Handle empty input (specification)
    if not records:
        return None

    # Sort and validate records, establish relationships
    sorted_records = sorted(records)
    _validate_records(sorted_records)
    nodes = _establish_relationships(sorted_records)

    return nodes[0]

# ---------------------------------------------
# Example usage and demonstration
# ---------------------------------------------

def main():
    """Main function to demonstrate the BuildTree function."""
    records = [
        Record(0, 0),
        Record(1, 0),
        Record(2, 0),
        Record(3, 1),
        Record(4, 1),
        Record(5, 2),
        Record(6, 2),
    ]
    root = BuildTree(records)
    print(f"Root Node ID: {root.node_id}")
    for child in root.children:
        print(f"  Child Node ID: {child.node_id}, \n"
              f"    Children: {[c.node_id for c in child.children]}")

if __name__ == "__main__":
    main()

# ---------------------------------------------
# Additional utility for inspecting dataclasses
# ---------------------------------------------

    def inspect_dataclass(cls) -> None:
        """Print field metadata for a dataclass `cls` (use dataclasses.fields)."""
        print(f"Dataclass: {cls.__name__}")
        for f in fields(cls):
            default = f.default if f.default is not MISSING else None
            df = f.default_factory if f.default_factory is not MISSING else None
            df_name = getattr(df, "__name__", df) if df is not None else None
            print(f"  {f.name}: type={f.type!r}, default={default!r}, default_factory={df_name!r}")
