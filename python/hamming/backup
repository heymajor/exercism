def distance(strand_a, strand_b):
    counter = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    for index, line in enumerate(strand_a):
        # print(line)
        if strand_a[index] != strand_b[index]:
            counter += 1

    return counter


# print(distance("GGACGGATTCTG", "AGGACGGATTCT"))
