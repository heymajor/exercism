import re
from math import gcd

def clean(text):
    text = re.sub(r'[^a-zA-Z0-9]', '', text)
    text = text.lower()
    return text


def mmi(a):
    m = 26
    for x in range(0, m):
        if (a * x) % m == 1: 
            return x
    

def encode(plain_text, a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)
    encoded = []
    m = 26
    if gcd(a, m) != 1: raise ValueError("a and m must be coprime.")
    plain_text = clean(plain_text)
    plain_list = list(plain_text)
    for letter in plain_list:
        if letter.isnumeric():
            encoded.append(letter)            
            continue
        else:
            euclidX = ((a * alphabet.index(letter) + b) % m)
            encoded.append(alphabet[euclidX])            
    encoded = "".join(encoded)
    encoded = [encoded[i:i+5] for i in range(0, len(encoded), 5)]
    return " ".join(encoded)
    
def decode(ciphered_text, a, b):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet = list(alphabet)
    decoded = []
    m = 26
    if gcd(a, m) != 1: raise ValueError("a and m must be coprime.")
    ciphered_text = clean(ciphered_text)
    ciphered_list = list(ciphered_text)
    for cipher in ciphered_list:
        if cipher.isnumeric():
            decoded.append(cipher)
        else:
            y = alphabet.index(cipher)
            a_inv = mmi(a)
            euclidY = a_inv * (y - b) % m
            decoded.append(alphabet[int(euclidY)])
    return "".join(decoded)


def main():
    # print(encode("yes", 5, 7)) # xbt
    # print(mmi(15, 26))
    # print(decode("qdwju nqcro muwhn odqun oppmd aunwd o", 19, 16)) # anobstacleisoftenasteppingstone
    # print(decode("odpoz ub123 odpoz ub", 25, 7)) # testing123testing
    # print(encode("mindblowingly", 11, 15)) # rzcwa gnxzc dgt
    # print(decode("tytgn fjr", 3, 7)) # exercism
    # print(encode("OMG", 21, 3)) # lvz
    # print(encode("Testing,1 2 3, testing.", 3, 4)) # jqgjc rw123 jqgjc rw
    print(decode("odpoz ub123 odpoz ub", 25, 7)) # testing123testing

if __name__ == '__main__':
    main()

"""
> The given formula `a ** -1` to find MMI is little incomplete and not as straightforward as it may seem. Have a read through this wikipedia section.

Oh man. I've never heard of an "abuse of notation", but I definitely considered `a` to be the inverse. 

To consolidate the `is_prime()`, `math.gcd(a, m)` is used to verify `a` and `m` are coprime in the form of `if gcd(a, m) != 1: raise ValueError("a and m must be coprime.")`.

> Do not ignore the mention of MMI in last bit of decrypting section and the dedicated "Example of finding MMI" section where you can test if you are generating right MMI for given 'a'. (when a=15 are you generating 7?).

I added a function `mmi()` to identify `a_inv` by iterating through `range(0, m)`. I know now that it's not technically an inverse of `a`, but it's where I'm at :)

A conditional statement was also added to the decode function to allow the numbers to pass through and include in the output. 

Thank you for your help!!
"""