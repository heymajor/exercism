class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        split_input = self.matrix_string.split("\n")
        return_row = split_input[index - 1].split(" ")
        return_row_int = map(int, return_row)
        return list(return_row_int)

    def column(self, index):
        split_input = self.matrix_string.split("\n")
        print(split_input)
        index -= 1
        return_col = []
        for n in split_input:
            n = n.split(" ")
            n = list(map(int, n))
            # print(n[index])
            return_col.append(n[index])
        # return_col_int = map(int, return_col)
        return list(return_col)


# matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
# print(matrix.row(4), [8, 7, 6])

# matrix = Matrix("1 2 3 4\n5 6 7 8\n9 8 7 6")
# print(matrix.column(4), [4, 8, 6])

# matrix = Matrix("89 1903 3\n18 3 1\n9 4 800")
# print(matrix.column(2), [1903, 3, 4])
