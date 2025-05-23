"""Functions which helps the locomotive engineer to keep track of the train."""

def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    args = list(args) # convert to list

    return args

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.
    
    The function ensures the locomotive (ID=1) is first,
    followed by the missing wagons, then the remaining wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    # Get a copy of the original list to avoid side effects
    # Find and remove locomotive (ID=1) and store it in a variable
    wagons = each_wagons_id.copy()
    locomotive = wagons.pop(wagons.index(1))

    # Handle the case with wagons 2 and 5
    # Add lists together with + (list concatenation)
    first, second, *rest = wagons
    train = [locomotive] + missing_wagons + rest + [first, second]

    return train

def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    updated_route = route.copy()
    
    stop_values = [value for _key, value in sorted(stops.items())]
    updated_route['stops'] = stop_values

    return updated_route

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    updated_route = route.copy()

    for key, value in more_route_information.items():
        # Update dict with new key-value pairs
        updated_route[key] = value

    return updated_route

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    wagons_rows = wagons_rows.copy()

    # Use zip to transpose the rows
    # Use list comprehension to create a new list of lists
    # * operator unpacks the outer list so that each of its elements (the inner lists) 
    # are passed as separate arguments to `zip()
    transposed_rows = [list(row) for row in zip(*wagons_rows)]

    return transposed_rows
