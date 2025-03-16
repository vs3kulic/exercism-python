azara_record = ('treasure', 'coordinate')
rui_record = ('location', ('coordinate', 'coordinate_2'), 'quadrant')

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

print(create_record(azara_record, rui_record))