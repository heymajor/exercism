def list_verse(verse_number):
    verse = {
        1: "a Partridge in a Pear Tree",
        2: "two Turtle Doves",
        3: "three French Hens",
        4: "four Calling Birds",
        5: "five Gold Rings",
        6: "six Geese-a-Laying",
        7: "seven Swans-a-Swimming",
        8: "eight Maids-a-Milking",
        9: "nine Ladies Dancing",
        10: "ten Lords-a-Leaping",
        11: "eleven Pipers Piping",
        12: "twelve Drummers Drumming",
    }
    return verse.get(verse_number)


# print(list_verse(2))


def days(day):
    days = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth",
    }
    return days.get(day)


# print(days(3))


def sing(start_verse):
    global output_element
    output_element = ""
    output_element = (
        f"On the {days(start_verse)} day of Christmas my true love gave to me: "
    )
    if start_verse == 1:
        ending = "a Partridge in a Pear Tree."
    else:
        ending = "and a Partridge in a Pear Tree."

    while start_verse > 1:
        output_element += f"{list_verse(start_verse)}, "
        start_verse -= 1

    output_element += ending
    return "".join(output_element)


def recite(start_verse, end_verse):
    verse_to_sing = start_verse
    output = []
    while verse_to_sing <= end_verse:
        output.append(sing(verse_to_sing))
        verse_to_sing += 1
    return output


# expected = [
#     "On the second day of Christmas my true love gave to me: "
#     "two Turtle Doves, "
#     "and a Partridge in a Pear Tree."
# ]

# expected = [
#     "On the first day of Christmas my true love gave to me: "
#     "a Partridge in a Pear Tree."
# ]

# print(recite(1, 1) == expected)
# print(recite(1, 1))
# print(expected)


# expected = [
#     "On the eighth day of Christmas my true love gave to me: "
#     "eight Maids-a-Milking, "
#     "seven Swans-a-Swimming, "
#     "six Geese-a-Laying, "
#     "five Gold Rings, "
#     "four Calling Birds, "
#     "three French Hens, "
#     "two Turtle Doves, "
#     "and a Partridge in a Pear Tree."
# ]


# print(recite(8, 8) == expected)
# print(recite(8, 8))
# print(expected)
# expected = [recite(n, n)[0] for n in range(4, 7)]
# print(recite(4, 6))
# print(expected)
