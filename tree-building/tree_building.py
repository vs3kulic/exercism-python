"""This module contains a function to build a tree from a list of records."""


class Record:
    """Class representing a record with an ID and a parent ID."""
    def __init__(self, record_id: int, parent_id: int) -> None:
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    """Class representing tree node with a node ID and children."""
    def __init__(self, node_id: int) -> None:
        self.node_id = node_id
        self.children = []


def BuildTree(records: list[Record]) -> Node:
    """Build a tree from a list of Record instances.
    
    :param records: List of Record instances
    :type records: list[Record]
    :returns: The root Node of the constructed tree
    :rtype: None
    """
    # Initialize root to None
    root = None

    # Sort Record instances by record_id
    # Extract list of ordered records
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id for i in records]
    
    # Validate the integrity of the records
    if records:
        # First record must be root (record_id 0)
        if ordered_id[0] != 0:
            raise ValueError('invalid')
        # Last record_id (zero-indexed) must match number of records to ensure continuity
        if ordered_id[-1] != len(ordered_id) - 1:
            raise ValueError('broken tree')

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
