import re 

def count_words(sentence):
    # regex = re.compile('[,\.!?]')
    # print(regex.sentence())
    # sentence = sentence.replace(","," ")
    # sentence = sentence.replace("_"," ")
    sentence = re.sub("[^a-zA-Z0-9 \']"," ",sentence)
    sentence = sentence.lower()
    sentence = sentence.split(" ")   
    sentence = " ".join(sentence)  
    sentence = " ".join(sentence.split())  
    sentence = sentence.split(" ")   
    sentence = [word.strip("'") for word in sentence]

    # print(sentence)
    # print(type(sentence))
    output = set()
    output = {word: sentence.count(word) for word in sentence}
    return output



# print(count_words("one fish two fish red fish blue fish"))
# # {"one": 1, "fish": 4, "two": 1, "red": 1, "blue": 1}

print(count_words(",\n,one,\n ,two \n 'three'"))
#  {"one": 1, "two": 1, "three": 1}
print(count_words("one,two,three"))
print(count_words("testing, 1, 2 testing"))
# print(count_words("Joe can't tell between app, apple and a."))
print(count_words(",\n,one,\n ,two \n 'three'"))