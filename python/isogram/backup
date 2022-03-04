def is_isogram(string):
    string = string.lower()
    string = string.replace(" ","")
    string = string.replace("-","")
    if len(string) == 0: return True
    string = list(string)
    for letter in string:
        if string.count(letter) > 1:
            return False
        else:
            continue    
    return True
    # letters = set()
    # letters = {letter: string.count(letter) for letter in string}
    # for i in letters:
    #     print(i)
    # letters = dict(letters)

    # for key, value in letters.items():
    #     if  value > 1:
    #         return False
    #     else:
    #         return True

# print(is_isogram("isograms"))
# print(is_isogram(""))
# print(is_isogram("thumbscrew-japingly"))
