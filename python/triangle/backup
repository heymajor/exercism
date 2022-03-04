def eq(a, b):
    return a == b


def neq(a, b):
    return a != b


def verify_length(a, b, c):
    return a + b > c and a + c > b and b + c > a


def assign_sides(sides):
    side1, side2, side3 = [sides[i] for i in (0, 1, 2)]
    return side1, side2, side3


def equilateral(sides):
    a, b, c = assign_sides(sides)
    return (
        eq(a, b) and eq(b, c) and eq(c, a) and 0 not in sides and verify_length(a, b, c)
    )


# print(equilateral([2, 2, 2]))
# print(equilateral([0, 0, 0]))


def isosceles(sides):
    a, b, c = assign_sides(sides)
    return (
        (eq(a, b) or eq(b, c) or eq(c, a)) and 0 not in sides and verify_length(a, b, c)
    )


# print(isosceles([3, 1, 1]))
# print(verify_length(1, 1, 3))


def scalene(sides):
    a, b, c = assign_sides(sides)
    return (
        neq(a, b)
        and neq(b, c)
        and neq(c, a)
        and 0 not in sides
        and verify_length(a, b, c)
    )


# print(scalene([7, 3, 2]))
