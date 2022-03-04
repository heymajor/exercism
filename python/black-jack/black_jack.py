"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def is_ten(card):
    tens = ["K", "J", "Q", "10"]
    return card in tens


def is_ace(card):
    return card == "A"


def is_face(card):
    face = ["A", "K", "J", "Q"]
    return card in face


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    """
    if is_face(card):
        if is_ace(card):
            return 1
        else:
            return 10
    else:
        return int(card)


# print(value_of_card("K"))
# print(value_of_card("1"))
# print(value_of_card("4"))


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 1; numerical value otherwise.
    :return: higher value card - str. Tuple of both cards if they are of equal value.
    """
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one_value == card_two_value:
        return card_one, card_two
    if card_one_value > card_two_value:
        return card_one
    else:
        return card_two


# print(higher_card("K", "10"))
# print(higher_card("4", "6"))
# print(higher_card("K", "A"))


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. 'J', 'Q', 'K' = 10; 'A' = 11 (if already in hand); numerical value otherwise.
    :return: int - value of the upcoming ace card (either 1 or 11).
    """
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if is_ace(card_one) or is_ace(card_two):
        return 1
    elif (card_one_value + card_two_value) <= 10:
        return 11
    else:
        return 1


# print(value_of_ace("K", "6"))
# print(value_of_ace("7", "3"))
# print(value_of_ace("A", "2"))


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - cards dealt. 'J', 'Q', 'K' = 10; 'A' = 11; numerical value otherwise.
    :return: bool - if the hand is a blackjack (two cards worth 21).
    """
    return (is_ace(card_one) and is_ten(card_two)) or (
        (is_ace(card_two)) and is_ten(card_one)
    )


# print(is_blackjack("A", "K"))
# print(is_blackjack("A", "3"))


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - if the hand can be split into two pairs (i.e. cards are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)


# print(can_split_pairs("Q", "K"))
# print(can_split_pairs("10", "A"))
# print(can_split_pairs("2", "3"))


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - if the hand can be doubled down (i.e. totals 9, 10 or 11 points).
    """
    double_down = [9, 10, 11]
    return (value_of_card(card_one) + value_of_card(card_two)) in double_down


# print(can_double_down("A", "9"))
# print(can_double_down("10", "2"))
