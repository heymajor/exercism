def rotate(text, key):
    plain = list("abcdefghijklmnopqrstuvwxyz")
    acceptable_characters = list(" .!',123456789")

    upper_flag = False
    output = []
    cipher = plain[key:len(plain)] + plain[:key]
    cipher = list(cipher)
    text = list(text)
    for letter in text:
        upper_flag = False
        if letter == letter.upper():
            upper_flag = True
            letter = letter.lower()
        if letter in acceptable_characters: 
            output.append(letter)
            continue
        i = plain.index(letter)
        if upper_flag:
            output.append(cipher[i].upper())
        else:
            output.append(cipher[i])
    return "".join(output)

def main():
    # print(rotate("a",1)) # b
    # print(rotate("The quick brown fox jumps over the lazy dog.", 13)) # Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
    print(rotate("Let's eat, Grandma!", 21)) # Gzo'n zvo, Bmviyhv!

if __name__ == '__main__':
    main()