def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
        quit()
    x = 1
    for _ in range(1, number):
        # print(_)
        x *= 2
    return x


# print(square(65))


def total():
    

