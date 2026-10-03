def rotate(matrix):
    n=len(matrix)

    #transpose the matrix
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    #reverse the matrix
    for i in range(n):
        matrix[i].reverse()

    return matrix

def main():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print("Original Matrix:")
    for row in matrix:
        print(row)

    rotated_matrix = rotate(matrix)

    print("\nRotated Matrix by 90 degrees:")
    for row in rotated_matrix:
        print(row)


if __name__ == "__main__":
    main()

    
