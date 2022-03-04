import re

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = "".join(list(set(sentence.lower())))
    regex = r"[^a-z]"
    sentence = re.sub(regex,"",sentence)
    return sorted(sentence) == sorted(alphabet)


def main():
    # print(is_pangram('"Five quacking Zephyrs jolt my wax bed."'))
    print(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"))

if __name__ == '__main__':
    main()