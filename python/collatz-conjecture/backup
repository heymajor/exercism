def steps(n):
    counter = 0
    if n <= 0:         
        raise ValueError("Only positive integers are allowed")

    while n > 1:
        counter += 1
        if counter > 1000: break
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
    return counter


# def main():
#     print(steps(0))

# if __name__ == "__main__":
#     main()