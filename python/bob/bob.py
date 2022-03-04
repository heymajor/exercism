import re

def response(hey_bob):
    hey_bob = re.sub(r"[^a-zA-Z0-9\?]", "", hey_bob)
    print(len(hey_bob))
    hey_bob_list = list(hey_bob)
    flag_lowercase = False
    flag_uppercase = False
    flag_question = False

    if len(hey_bob) == 0: return "Fine. Be that way!"

    if hey_bob[-1] == "?": flag_question = True

    for letter in hey_bob_list:
        if letter.islower(): flag_lowercase = True 
        if letter.isupper(): flag_uppercase = True
    
    if flag_uppercase and flag_lowercase is False and flag_question is False: return "Whoa, chill out!"

    if flag_uppercase and flag_lowercase is False and flag_question: return "Calm down, I know what I'm doing!"

    if flag_question: return "Sure."

    return "Whatever."
