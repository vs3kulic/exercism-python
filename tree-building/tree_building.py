"""This module contains a function to build a tree from a list of records."""
from __future__ import annotations


class Record:
    """Class representing a record with an ID and a parent ID."""
    def __init__(self, record_id: int, parent_id: int):
        self.record_id = record_id
        self.parent_id = parent_id
    
    # Define less-than for sorting
    def __lt__(self, other: Record) -> bool:
        """Compare two Record instances based on their record_id."""
        return self.record_id < other.record_id


class Node:
    """Class representing tree node with a node ID and children."""
    def __init__(self, node_id: int):
        self.node_id = node_id
        self.children = []


def _validate_records(sorted_records: list[Record]) -> None:
    """Validate the integrity of the records.
    
    :param sorted_records: Sorted list of Record instances
    :type sorted_records: list[Record]
    :raises ValueError: If records do not form a valid tree structure
    """
    # First record must be root (record_id 0)
    if sorted_records[0].record_id != 0:
        raise ValueError("Record id is invalid or out of order.")

    # Last record_id (zero-indexed) must match number of records to ensure continuity
    if sorted_records[-1].record_id != len(sorted_records) - 1:
        raise ValueError("Record id is invalid or out of order.")

    # Parent-child relationship rules
    if any(record.record_id < record.parent_id for record in sorted_records):
        raise ValueError("Node parent_id should be smaller than its record_id.")

    if any((record.record_id == record.parent_id and record.record_id != 0)
           for record in sorted_records):
        raise ValueError("Only root should have equal record and parent id.")


def _establish_relationships(sorted_records: list[Record]) -> list[Node]:
    """Create Node instances for each record and establish parent-child links.

    This helper returns the created list of nodes so callers can access the
    root. It combines node creation and linking into a single helper.

    :param sorted_records: List of Record instances (already sorted by record_id)
    :type sorted_records: list[Record]
    :returns: List of Node instances with children linked
    :rtype: list[Node]
    """
    # Create all nodes
    nodes = [Node(record.record_id) for record in sorted_records]

    # Establish parent-child relationships
    for record in sorted_records:
        if record.record_id == 0:
            continue  # Skip root node
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
