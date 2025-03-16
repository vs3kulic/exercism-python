"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can't eat a ghost if he is not empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?
    """
    if not power_pellet_active and touching_ghost:
        return False
    if power_pellet_active and not touching_ghost:
        return False
    return power_pellet_active and touching_ghost

def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """
    if touching_power_pellet or touching_dot:
        return True
    if not touching_power_pellet and not touching_dot: 
        return False
    return touching_power_pellet and touching_dot

def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    if not power_pellet_active and touching_ghost:
        return True
    if power_pellet_active and touching_ghost: 
        return False
    if not touching_ghost:
        return False
    return power_pellet_active and touching_ghost

def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """
    if has_eaten_all_dots and not power_pellet_active and not touching_ghost:
        return True
    if has_eaten_all_dots and power_pellet_active and touching_ghost:
        return True
    if has_eaten_all_dots and not power_pellet_active and touching_ghost:
        return False
    if not has_eaten_all_dots: 
        return False
    return has_eaten_all_dots and power_pellet_active and not touching_ghost
