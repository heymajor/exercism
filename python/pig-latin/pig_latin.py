vowels = ["a", "e", "i", "o", "u", "y"]
two_letters = ["qu", "ch", "th"]
three_letters = ["thr", "sch"]

def translate(text):
    text_list = text.split(" ")
    temp = []
    for word in text_list:
        temp.append(trans(word))
    return " ".join(temp)


def trans(text):
    if len(text) > 2:
        if text[0] == "y" and text[1] in vowels:
            return text[1:] + text[0:1] + "ay"

        elif text[0] in vowels or text[0:2] == "xr":
            return text + "ay"
        elif text[0:3] in three_letters or text[1:3] == "qu": 
            return text[3:] + text[0:3] + "ay"
        elif text[0:2] in two_letters or text[2] == "y": 
            return text[2:] + text[0:2] + "ay"
        else:
            return text[1:] + text[0] + "ay"
    else:
        if text[1] == "y":
            return text[1:] + text[0] + "ay"
    



# def main():
#     # phrase = "ear" # earay
#     # phrase = "apple" # appleay
#     # phrase = "queen" # eenquay
#     # phrase = "therapy" # erapythay
#     # phrase = "thrush" # ushthray
#     # phrase = "xray" # xrayay
#     # phrase = "yttria" # yttriaay
#     # phrase = "yellow" # ellowyay
#     # phrase = "my" # ymay
#     phrase = "quick fast run"
#     print(translate(phrase)) 


# if  __name__ == "__main__":
#     main()