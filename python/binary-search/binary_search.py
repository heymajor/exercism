def find(search_list, value):

    for n in search_list:
        if n == value: 
            return search_list.index(value)

    raise ValueError("value not in array")

# def main():
#     # print(find([1, 3, 4, 6, 8, 9, 11], 6)) # 3
#     # print(find([1, 3, 4, 6, 8, 9, 11], 13)) # ValueError
#     print(find([1, 3, 4, 6, 8, 9, 11], 11)) # 6

# if __name__ == '__main__':
#     main()