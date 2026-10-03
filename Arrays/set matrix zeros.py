def setzeros(matrix):
    rows=len(matrix)
    cols=len(matrix[0])

    zero_rows=set()
    zero_cols=set()

    #find the rows and columns that need to be set to zero
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0:
                zero_rows.add(i)
                zero_cols.add(j)

    #set the identified rows and columns to zero
    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j]=0

    return matrix

def main():
    matrix = [[1, 2, 3],
              [4, 0, 6],
              [7, 8, 9]]

    print("Original Matrix:")
    for row in matrix:
        print(row)

    modified_matrix = setzeros(matrix)

    print("\nMatrix after setting zeros:")
    for row in modified_matrix:
        print(row)


if __name__ == "__main__":
    main()