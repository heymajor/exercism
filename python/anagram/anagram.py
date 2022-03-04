def find_anagrams(word, candidates):
    output = []
    for candidate in candidates:
        if sorted(candidate.lower()) == sorted(word.lower()) and candidate.lower() != word.lower():
            output.append(candidate)
    return output            


def main():

    # candidates = ["lemons", "cherry", "melons"]
    # print(find_anagrams("solemn", candidates)) # ["lemons", "melons"]

    # candidates = ["lemons", "cherry", "melons"]
    # print(find_anagrams("cherrry", candidates)) # []

    # candidates = ["lemons", "cherry", "melons"]
    # print(find_anagrams("yrherc", candidates)) # ["cherry"]

    # candidates = ["hello", "world", "zombies", "pants"]
    # print(find_anagrams("diaper")) # []

    candidates = ["BANANA", "Banana", "banana"]
    print(find_anagrams("BANANA", candidates)) # []

if __name__ == '__main__':
    main()
