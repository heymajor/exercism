def triplets_with_sum(n):
    solutions = []
    for a in range(1, n):
        denom = 2 * (n - a)
        num = (2 * a**2) + n**2 - (2 * n * a)
        if denom > 0 and num % denom == 0:
            c = num // denom
            b = n - a - c
            if b > a:
                solutions.append((a, b, c))
    solutions = [list(x) for x in solutions]
    print(solutions)

    return solutions

# reference: https://stackoverflow.com/questions/61755082/pythagorean-triplet-with-given-sum
