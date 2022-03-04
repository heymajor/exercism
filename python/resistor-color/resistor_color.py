def color_code(col):
    colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"] 
    for color in colors: 
        if col == color:
            return colors.index(color)

def colors():
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"] 


# def main():
#     print(color_code("black")) # 0
#     print(color_code("white")) # 9
#     print(color_code("orange")) # 3

# if __name__ == '__main__':
#     main()