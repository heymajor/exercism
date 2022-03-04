SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    one_chars = map(str, list_one)
    two_chars = map(str, list_two)
    list_one_str = ",".join(one_chars) + ","
    list_two_str = ",".join(two_chars) + ","

    if list_one_str == list_two_str:
        return 2
    elif list_one_str in list_two_str or list_one_str == []:
        return 0
    elif list_two_str in list_one_str or list_two_str == []:
        return 1
    else:
        return 3
