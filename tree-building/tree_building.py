"""This module contains a function to build a tree from a list of records."""


class Record:
    """Class representing a record with an ID and a parent ID."""
    def __init__(self, record_id: int, parent_id: int) -> None:
        self.record_id = record_id
        self.parent_id = parent_id
        
    def __lt__(self, other: "Record") -> bool:
        """Compare two Record instances based on their record_id."""
        return self.record_id < other.record_id


class Node:
    """Class representing tree node with a node ID and children."""
    def __init__(self, node_id: int) -> None:
        self.node_id = node_id
        self.children = []

def _sort_records(records: list[Record]) -> list[int]:
    """Sort records by their record_id.
    
    :param records: List of Record instances
    :type records: list[Record]
    :returns: Sorted list of Record instances
    :rtype: list[Record]
    """
    # Sort Record instances by record_id
    # records.sort()
    ordered_id = [record.record_id for record in sorted(records)]
    return ordered_id

def _validate_records(ordered_id: list[int]) -> None:
    """Validate the integrity of the records.
    
    :param records: List of Record instances
    :type records: list[Record]
    :raises ValueError: If records do not form a valid tree structure
    """
    if ordered_id:
        # First record must be root (record_id 0)
        if ordered_id[0] != 0:
            raise ValueError('invalid')
        # Last record_id (zero-indexed) must match number of records to ensure continuity
        if ordered_id[-1] != len(ordered_id) - 1:
            raise ValueError('broken tree')

def BuildTree(records: list[Record]) -> Node:
    """Build a tree from a list of Record instances.
    
    :param records: List of Record instances
    :type records: list[Record]
    :returns: The root Node of the constructed tree
    :rtype: None
    """
    # Initialize root (to None)
    root = None

    # Sort and validate records
    ordered_id = _sort_records(records)
    _validate_records(records)

    # Initialize list to hold Node instances
    # Initialize parent mapping
    trees = []
    parent = {}
    
    # Add Node instances to trees list
    for i in range(len(ordered_id)):
        for j in records:
            if ordered_id[i] == j.record_id:
                # Validate parent-child relationships
                if j.record_id == 0:
                    if j.parent_id != 0:
                        raise ValueError('error!')
                # Validate that no record has a parent_id greater than its record_id
                if j.record_id < j.parent_id:
                    raise ValueError('something went wrong!')
                # Validate that non-root records are not their own parents
                if j.record_id == j.parent_id:
                    if j.record_id != 0:
                        raise ValueError('error!')
                # Create Node and add to trees list
                trees.append(Node(ordered_id[i]))
    
    # Build the tree structure by linking parents and children
    for i in range(len(ordered_id)):
        # Find parent Node for current record
        for j in trees:
            if i == j.node_id:
                parent = j
        # Find and attach child Nodes to the parent Node
        for j in records:
            if j.parent_id == i:
                for k in trees:
                    # Skip the root node when attaching children
                    if k.node_id == 0:
                        continue
                    # Attach child to parent
                    if j.record_id == k.node_id:
                        child = k
                        parent.children.append(child)

    # Set the root node and return
    if len(trees) > 0:
        root = trees[0]
    return root
