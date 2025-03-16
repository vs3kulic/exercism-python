"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    non_digit = {"K": 10, "Q": 10, "J": 10, "A": 1}

    if card.isdigit():
        return int(card)
    
    return non_digit[card]


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one) == value_of_card(card_two):
        return (card_one, card_two)
    
    return max((card_one, card_two), key=value_of_card)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    current_total = 0
    num_aces = 0

    # Calculate initial total with aces as 11
    for card in [card_one, card_two]:
        if card == "A":
            current_total += 11
            num_aces += 1
        else:
            current_total += value_of_card(card)

    # Adjust for aces if over 21
    while current_total > 21 and num_aces > 0:
        current_total -= 10
        num_aces -= 1

    # Determine ace value (11 if adding it doesn't bust)
    if (current_total + 11) <= 21: 
        return 11 
    return 1