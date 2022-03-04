import math


def rebase(input_base, digits, output_base):
    error(input_base, digits, output_base)
    if len(digits) == 0 or sum(digits) == 0: return [0]
    i = reversed(range(len(digits)))
    digits.reverse()
    number = sum([(input_base**x)*digits[x] for x in i])
    power = largest_power(number, output_base)
    temp_list = []
    quotient = 0
    while power >= 0:
        quotient = int(number/output_base**power)
        temp_list.append(quotient)
        if (number - (quotient * output_base**power)) >= 0: 
            number -= (quotient * output_base**power)
        power -= 1
    return temp_list


def largest_power(n, base):
    return int(math.log(n, base))

    
def error(input_base, digits, output_base):
    if input_base < 2: raise ValueError("input base must be >= 2")
    if output_base < 2: raise ValueError("output base must be >= 2")
    if any(d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if any(d < 0 for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    return

def main():
    # print(rebase(2, [1, 0, 1, 0, 1, 0], 10)) # [4, 2]
    # print(rebase(2, [1], 10))
    # print(rebase(10, [4, 2], 2)) # [1, 0, 1, 0, 1, 0]
    # print(rebase(2, [], 10))  # [0]
    print(rebase(2, [1, 2, 1, 0, 1, 0], 10)) # error: "all digits must satisfy 0 <= d < input base"

if __name__ == '__main__':
    main()