def score(word):
    total = []
    letters = list(word)
    for letter in letters:
        total.append(count(letter))
    # print(total)
    return sum(total)

def count(x):
    x = x.upper()
    if x in ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]:
        return 1
    if x in ["D", "G"]:
        return 2
    if x in ["B", "C", "M", "P"]:
        return 3
    if x in ["F", "H", "V", "W", "Y"]:
        return 4
    if x in ["K"]:
        return 5
    if x in ["J", "X"]:
        return 8
    if x in ["Q", "Z"]:
        return 10
def main():
    print(score("zoo"))

if __name__ == '__main__':
    main()

