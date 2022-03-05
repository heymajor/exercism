import numpy as np

def saddle_points(matrix):
    matrix = np.array(matrix)

    height = len(matrix[:,-1])
    width = len(matrix[-1,:])
    # print(max(matrix[:,-1]))
    # coord = np.where(matrix[:,-1] == max(matrix[:,-1]))
    coord = np.where(matrix == 7)
    print(len(coord))
    print(coord)
    # # Row comparison:
    # for i in range(height):
    #     for j in range(width):
    #         print("i:",i)
    #         print("j:",j)
    #         print(matrix[i,j])
    #         print("---")
    #         # y = matrix[:,i]
    #         # print(y)

    ## Column comparison:
    # for j in range(width):
    #     for i in range(height):
    #         print("i:",i)
    #         print("j:",j)
    #         print(matrix[i,j])
    #         print("---")
    #         # y = matrix[:,i]
    #         # print(y)




"""
"saddle point" conditions: (point >= row_elements) or (point <= col_elements)

Identify matrix columns with provided matrix rows

Use NumPy to manipulate and compare matrix elements
"""

def main():
    matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
    print(saddle_points(matrix))

if __name__ == '__main__':
    main()