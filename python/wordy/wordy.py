def answer(question):
    question = question.replace("plus","+")
    question = question.replace("minus","-")
    question = question.replace("divided by","/")
    question = question.replace("multiplied by","*")
    question = question.replace("What is ","")
    question = question.replace("?","")
    # question = question.split(" ")
    return eval
    # return question
    # return eval(question)

def main():
    # print(answer("What is 33 divided by -3?")) # -11
    print(answer("What is -3 plus 7 multiplied by -2?")) # -8

if __name__ == '__main__':
    main()

"""
([+-]?(?=\.\d|\d)(?:\d+)?(?:\.?\d*))(?:[eE]([+-]?\d+))?.*\+\-\*\/.*[0-9]
"""