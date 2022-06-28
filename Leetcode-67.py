if __name__ == "__main__":
    a = input()
    b = input()
    binary1 = "0b"+str(a)
    binary2 = "0b"+str(b)
    integer_sum = int(binary1, 2) + int(binary2, 2)
    binary_sum = bin(integer_sum)
    print(binary_sum[2::])