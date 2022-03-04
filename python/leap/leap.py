def leap_year(year):
    if div_by_4(year):
        if div_by_100(year):
            if div_by_400(year):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def div_by_4(x):
    return x % 4 == 0

def div_by_400(x):
    return x % 400 == 0

def div_by_100(x):
    return x % 100 == 0

  