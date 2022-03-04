# Score categories.
# Change the values as you see fit.

YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"
little_straight = {1, 2, 3, 4, 5}
big_straight = {2, 3, 4, 5, 6}


def score(dice, category):
    if category == ONES:
        return dice.count(1)
    if category == TWOS:
        return 2 * dice.count(2)
    if category == THREES:
        return 3 * dice.count(3)
    if category == FOURS:
        return 4 * dice.count(4)
    if category == FIVES:
        return 5 * dice.count(5)
    if category == SIXES:
        return 6 * dice.count(6)
    if category == FULL_HOUSE:
        temp_set = set(dice)
        toggle_three = 0
        toggle_two = 0
        out = 0
        for token in temp_set:
            print(dice.count(token))
            if dice.count(token) == 3:
                toggle_three += 1
                out += 3 * token
            if dice.count(token) == 2:
                toggle_two += 1
                out += 2 * token
        if toggle_three == 1 and toggle_two == 1:
            return out
        else:
            return 0
    if category == CHOICE:
        return sum(dice)
    if category == FOUR_OF_A_KIND:
        out = 0
        for token in dice:
            if dice.count(token) >= 4:
                out = 4 * token
        return out
    if category == LITTLE_STRAIGHT:
        if little_straight.issubset(set(dice)):
            return 30
        else:
            return 0
    if category == BIG_STRAIGHT:
        if big_straight.issubset(set(dice)):
            return 30
        else:
            return 0  
    if category == YACHT:
        for token in dice:
            if dice.count(token) == 5:
                return 50
            else:
                return 0

# def main():
#     # print(score([3, 1, 1, 1, 1], FOUR_OF_A_KIND))
#     # print(score([3, 1, 1, 1, 1], LITTLE_STRAIGHT))
#     # print(set(numbers))
#     # print(score([5, 5, 5, 5, 5], YACHT))
#     # print(score([1, 4, 4, 4, 4],FULL_HOUSE))  # 0
#     # print(score([5, 3, 3, 5, 3],FULL_HOUSE))  # 19
#     print(score([3, 3, 3, 3, 3],FOUR_OF_A_KIND))  # 12


# if __name__ == "__main__":
#     main()