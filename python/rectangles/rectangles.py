import re


def rectangles(input):
    left = 0
    count = 0
    regex = r"(?<=\|).*(?=\|)"
    for thing in input: 
        if sum(1 for _ in re.finditer(regex, thing)):
        # for match in re.finditer(regex, thing):
        # print(sum(1 for _ in re.finditer(regex, thing)))
            count += 1  

    return count


def main():
    print(rectangles(["  +-+", "    |", "+-+-+", "| | -", "+-+-+"]))

if __name__ == '__main__':
    main()    

"""
https://regex101.com/

I'm not familiar with how to even start this
"""