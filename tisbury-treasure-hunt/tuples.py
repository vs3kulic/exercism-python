"""Functions to help Azara and Rui locate pirate treasure."""
azara_record = ('Scrimshawed Whale Tooth', '2A')
rui_record = ('Tisbury', ('2', 'A'), 'NE')

def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    map_coordinate = record[1]

    return map_coordinate


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    tuple = (coordinate[0], coordinate[1])
    
    return tuple


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    azara_coordinate = azara_record[1]
    rui_coordinates = rui_record[1][0] + rui_record[1][1]
    coordinate_match = (azara_coordinate == rui_coordinates)

    return coordinate_match


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    combined_record = ()
    
    if compare_records(azara_record, rui_record):
        combined_record = (azara_record+rui_record)
        return combined_record
    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.
    """
    cleaned_records = []

    for record in combined_record_group:
        # Structure: (treasure, azara_coord_str, location, rui_coord_tuple, quadrant)
        treasure = record[0]
        location = record[2]
        quadrant = record[4]
        
        azara_coord_str = record[1]
        split_coord = convert_coordinate(azara_coord_str)
        
        cleaned_record = (treasure, location, split_coord, quadrant)
        cleaned_records.append(f"{cleaned_record}\n")  # f-string for readability
    
    return "".join(cleaned_records) # joins list of strings into single string