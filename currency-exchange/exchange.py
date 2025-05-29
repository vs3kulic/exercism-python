"""
Functions for calculating steps in exchanging currency.

Python numbers documentation: 
https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
"""

def exchange_money(budget: float, exchange_rate: float) -> float:
    """
    :param budget: float - amount of money you are planning to exchange
    :param exchange_rate: float - unit value of the foreign currency (e.g. 1 USD = 0.85 EUR)
    :return: float - exchanged value of the foreign currency you can receive
    """
    exchanged_value = budget / exchange_rate

    return exchanged_value

def get_change(budget: float, exchanging_value: float) -> float:
    """
    :param budget: float - amount of money you own
    :param exchanging_value: float - amount of your money you want to exchange now
    :return: float - amount left of your starting currency after exchanging
    """
    change_value = budget - exchanging_value

    return change_value

def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """
    :param denomination: int - the value of a bill
    :param number_of_bills: int - total number of bills
    :return: int - calculated value of the bills
    """
    bills_value = denomination * number_of_bills

    return bills_value

def get_number_of_bills(amount: float, denomination: int) -> int:
    """
    :param amount: float - the total starting value
    :param denomination: int - the value of a single bill
    :return: int - number of bills that can be obtained from the amount
    """
    bill_number = int(amount // denomination)

    return bill_number

def get_leftover_of_bills(amount: float, denomination: int) -> float:
    """
    :param amount: float - the total starting value
    :param denomination: int - the value of a single bill
    :return: float - the amount that is "leftover", given the current denomination
    """
    leftover_value = amount % denomination

    return leftover_value

def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """
    :param budget: float - the amount of your money you are planning to exchange
    :param exchange_rate: float - the unit value of the foreign currency
    :param spread: int - percentage that is taken as an exchange fee
    :param denomination: int - the value of a single bill
    :return: int - maximum value you can get
    """
    # Calculate exchange rate with spread fee
    rate_with_spread = exchange_rate * (1 + spread / 100)

    # Get foreign currency amount after exchange
    foreign_currency_amount = exchange_money(budget, rate_with_spread)

    # Calculate how many complete bills we can get
    number_of_bills = get_number_of_bills(foreign_currency_amount, denomination)

    # Calculate total value of those bills
    total_bill_value = get_value_of_bills(denomination, number_of_bills)

    return total_bill_value
