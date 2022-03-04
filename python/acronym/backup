def abbreviate(words):
    words = words.replace("-", " ")
    words = words.split()
    output = ""
    for word in words:
        if word[:1].isalpha():
            output += word[:1]
        else:
            output += word[1:2]
    output = output.upper()
    return output
