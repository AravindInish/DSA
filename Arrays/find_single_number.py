def  find_single_num(num):
    unique_num = 0
    for nums in num:
        unique_num ^= nums
    return unique_num

def main():
    num = [4, 1, 2, 1, 2]
    print("The single number is:", find_single_num(num))

if __name__ == "__main__":
    main()