def getRow(rowIndex):
    row = [1]

    for i in range(rowIndex):
        new_row = [1]

        for j in range(1, len(row)):
            new_row.append(row[j - 1] + row[j])

        new_row.append(1)
        row = new_row

    return row

def main():
    rowIndex = 3
    print(f"Row {rowIndex} of Pascal's Triangle:", getRow(rowIndex))

if __name__ == "__main__":
    main()