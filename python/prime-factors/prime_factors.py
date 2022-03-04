from math import sqrt
def factors(value):
    factors = []
    #This will find how many time value can be divided by 2(find even prime factors)
    while(value%2==0):
        factors.append(2)
        value//=2
    #This will find how many time value can be divided by all odd prime factors(find all odd prime factors)
    n=int(sqrt(value))
    for i in range(3,n+1,2):
        while(value%i==0):
            factors.append(i)
            value//=i
    #It is to find the give value is itself prime
    if(value!=1):
        factors.append(value)
    return factors
