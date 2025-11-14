"""This module contains a function to add a gigasecond to a given datetime."""
from datetime import datetime, timedelta

def add(moment: datetime) -> datetime:
    """Add a gigasecond (1,000,000,000 seconds) to the given datetime.
    
    :param moment: The initial datetime
    :type moment: datetime
    :returns: A new datetime representing the moment 1 gigasecond later
    :rtype: datetime
    """
    gigasecond = timedelta(seconds=1e9) # 1_000_000_000 seconds
    return moment + gigasecond
