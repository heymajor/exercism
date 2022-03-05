def spiral_matrix(size):
    starting_list = [x for x in range(1, size**2 + 1)]
    out = ["" for x in range(size)]

    #create size by size matrix
    matrix = create_matrix(size, starting_list)
    cycle(size, starting_list)

def cycle(list, size):
    row_first = list[0:size]
    middle_vertical_range = size - 2
    start = middle_vertical_range + size
    end = start + size
    row_last = list[start:end][::-1]

    
def create_matrix(size,starting_list):
    matrix = []
    for i in range(0, size**2, size):
        matrix.append(starting_list[i:size + i])
    # print(f"Starting matrix: {matrix}")
    return matrix
    
    # res = []
    # while matrix:
    #     if matrix[0]:
    #         res.extend(matrix[0]) #first row
    #         matrix = matrix[1:] #As we are done with the first row, get rid of it
    #     if matrix and matrix[0]:
    #         for row in matrix:
    #             res.append(row.pop()) #right side
    #     if matrix:
    #         res.extend(matrix.pop()[::-1]) #bottom ([::-1] = reversed)
    #     if matrix and matrix[0]:
    #         for row in matrix[::-1]:
    #             res.append(row.pop(0)) #left side
    # res = create_matrix(size, res)
    # return res


# #Discovered response that gives the same result 
# def spiral_matrix(size):
#     starting_list = [x for x in range(1, size**2 + 1)]
#     remainder_list = starting_list
#     #create size by size matrix
#     matrix = create_matrix(size, starting_list)
#     # return create_matrix(size, calculate(matrix))
#     return calculate(matrix)

# def calculate(matrix):
#     numbers = []
#     if not matrix or not matrix[0]:
#         return numbers
#     elif isinstance(matrix[0], int):
#         return numbers + matrix
#     else:
#         if len(matrix) == 1:
#             return numbers + matrix[0]
#         if len(matrix[0]) == 1:
#             return numbers + [item.pop() for item in matrix]
#     numbers += matrix[0][:-1]
#     numbers += (cols := [*zip(*matrix)])[-1][:-1]
#     numbers += matrix[-1][::-1][:-1]
#     numbers += cols[0][::-1][:-1]
#     if rest := matrix[1:-1]:
#         return numbers + calculate([item[1:-1] for item in rest])
#     return numbers

# def create_matrix(size,starting_list):
#     matrix = []
#     for i in range(0, size**2, size):
#         matrix.append(starting_list[i:size + i])
#     # print(f"Starting matrix: {matrix}")
#     return matrix


"""
1 - Create the matrix 
2 - """

def main():
    # print(spiral_matrix(4)) #[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    # print(spiral_matrix(3)) #[[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    print(spiral_matrix(6))

if __name__ == '__main__':
    main()