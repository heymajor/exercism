def add_prefix_un(word):
    """

    :param word: str of a root word
    :return:  str of root word with un prefix

    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """
    temp_string = ["un", word]
    return "".join(temp_string)


def make_word_groups(vocab_words):
    """

    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """
    vocab_words.reverse()
    prefix = vocab_words.pop()
    new_list = [prefix]
    vocab_words.reverse()
    for i in range(len(vocab_words)):
        new_list.append(prefix + vocab_words[i])

    # print(new_list)
    return " :: ".join(new_list)


# print(
#     make_word_groups(
#         [
#             "inter",
#             "twine",
#             "connected",
#             "dependent",
#             "galactic",
#             "action",
#             "stellar",
#             "cellular",
#             "continental",
#             "axial",
#             "operative",
#             "disciplinary",
#         ]
#     )
# )


def remove_suffix_ness(word):
    """

    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.

    This function takes in a word and returns the base word with `ness` removed.
    """
    # print(word[:-4])
    word = word[:-4]
    if word[-1] == "i":
        return word[:-1] + "y"
    else:
        return word


def adjective_to_verb(sentence, index):
    """

    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    sentence = sentence.split()
    if index == -1:
        # print(sentence[index])
        temp = sentence[index]
        sentence[index] = temp[:-1]
        # print(sentence[index])
    return sentence[index] + "en"


# print(adjective_to_verb("I need to make that bright.", -1))
# print(adjective_to_verb("It got dark as the sun set.", 2))
