def get_rounds(number):
    """

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    number_list = []
    for _ in range(3):
        number_list.append(number)
        number += 1
    return number_list


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    round_list = rounds_1 + rounds_2
    return round_list


def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """
    print(hand[0])
    print(hand[-1])
    avg = float((hand[0] + hand[-1]) / 2)
    middle = int((len(hand)) / 2)
    middle = float(hand[middle])
    actual = float(card_average(hand))
    return avg == actual or middle == actual


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    list_odd = []
    list_even = []
    for i, card in enumerate(hand):
        if i % 2 == 0:
            list_even.append(card)
        else:
            list_odd.append(card)
    return card_average(list_even) == card_average(list_odd)


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
