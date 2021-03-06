def largest(min_factor=0, max_factor=1):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    x = min_factor
    y = max_factor
    palindromes = find_palindromes(x, y)
    # print(palindromes)
    max_factor = int(palindromes[-1])
    # print(max_factor)
    temp = factors(max_factor, x, y)
    temp = [list(i) for i in set(map(tuple, temp))]
    # print(temp)

    return (max_factor, [list(i) for i in set(map(tuple, temp))])


def smallest(min_factor=0, max_factor=1):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    x = min_factor
    y = max_factor
    palindromes = find_palindromes(x, y)
    # print(palindromes)
    min_factor = int(palindromes[0])
    # print("min_factor:", min_factor)
    temp = factors(min_factor, x, y)
    temp = [list(i) for i in set(map(tuple, temp))]
    # print("temp:", temp)

    return (min_factor, [list(i) for i in set(map(tuple, temp))])


def factors(n, x, y):
    facts = []
    for a in range(1, n + 1):
        if n % a == 0:
            fact1 = a
            fact2 = int(n / a)
            if fact1 in range(x, y + 1, 1) and fact2 in range(x, y + 1, 1):
                temp = [fact1, fact2]
                temp.sort()
                facts.append(temp)
    return facts

def find_palindromes(min_factor, max_factor):
    temp_list = [*range(min_factor, max_factor + 1, 1)]
    if len(temp_list) <= 2: return ("", [])
    temp_factor_list = []
    palindromes = []

    for i in temp_list:      # Calculates list of all possible factors
        for j in temp_list:
            temp_factor_list.append(j * i) 
    
    for factor in temp_factor_list:
        # print(factor)
        products = list(str(factor))
        if products == products[::-1]: # if products is equal to its reverse
            palindromes.append("".join(products))
        else:
            pass

    # print(palindromes)
    palindromes = list(set(palindromes))
    palindromes = [int(i) for i in palindromes] # convert list str to int
    palindromes.sort()
    # print(palindromes)
    return palindromes


def main():
    print(largest(1, 9))
    # print(largest(min_factor=10, max_factor=99))
    # print(largest(min_factor=1000, max_factor=9999))
    # print(smallest(min_factor=10, max_factor=99))
    # print(smallest(min_factor=1, max_factor=9))
    # print(smallest(min_factor=1002, max_factor=1003))

if __name__ == '__main__':
    main()
