def spiral_matrix(mat):
    result = []

    top, bottom = 0, len(mat) - 1
    left, right = 0, len(mat[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(mat[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(mat[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1

    return result

def main():
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    print("Spiral order of the matrix is:", spiral_matrix(mat))

if __name__ == "__main__":
    main()