import re
class PhoneNumber:
    number = "0"
    area_code = ""
    exchange = ""
    last = ""


    def __init__(self, number):
        PhoneNumber.number = number
        PhoneNumber.clean(PhoneNumber.number)
        PhoneNumber.error(PhoneNumber.number)
        PhoneNumber.area_code = PhoneNumber.number[0:3]
        PhoneNumber.exchange = PhoneNumber.number[3:6]
        PhoneNumber.last = PhoneNumber.number[6:]

    def pretty(self):
        return f"({PhoneNumber.area_code})-{PhoneNumber.exchange}-{PhoneNumber.last}"

    def clean(x):
        if re.search('[a-zA-Z]', x): raise ValueError("letters not permitted")
        if re.search('[\@\:\!]', x): raise ValueError("punctuations not permitted")
        regex = r"[^0-9]"
        PhoneNumber.number = re.sub(regex,"", x)

    def error(x):
        if len(x) < 10: raise ValueError("incorrect number of digits")
        if len(x) > 11: raise ValueError("more than 11 digits")
        if len(x) == 10:
            if x[3] == "0": raise ValueError("exchange code cannot start with zero")
            if x[3] == "1": raise ValueError("exchange code cannot start with one")
            if x[0] == "0": raise ValueError("area code cannot start with zero")
            if x[0] == "1": raise ValueError("area code cannot start with one")
        if len(x) == 11:
            if x[0] != "1": raise ValueError("11 digits must start with 1")
            if x[1] == "0": raise ValueError("area code cannot start with zero")
            if x[1] == "1": raise ValueError("area code cannot start with one")
            if x[4] == "0": raise ValueError("exchange code cannot start with zero")
            if x[4] == "1": raise ValueError("exchange code cannot start with one")
            PhoneNumber.number = x[1:]




def main():
    # print(PhoneNumber("+1 (223) 456-7890").number)
    # print(PhoneNumber("223.456.7890").number) # 2234567890
    number = PhoneNumber("2234567890")
    # print(number.area_code) 
    print(number.pretty()) 

if __name__ == '__main__':
    main()

