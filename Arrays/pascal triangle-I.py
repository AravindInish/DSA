def generate(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def main():
    numRows = 5
    print("Pascal's Triangle:")
    triangle = generate(numRows)
    for row in triangle:
        print(row)

if __name__ == "__main__":
    main()