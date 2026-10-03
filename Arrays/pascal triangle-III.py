def pascalRow(r):
    row = [1]

    value = 1

    for i in range(1, r):
        value = value * (r - i) // i
        row.append(value)

    return row

def main():
    r = 5
    print(f"Row {r} of Pascal's Triangle:", pascalRow(r))

if __name__ == "__main__":
    main()