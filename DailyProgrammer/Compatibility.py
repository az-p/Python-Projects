def score(x, y):
    a = ~ (x ^ y) # XNOR
    return bin(a).count("1") / (bin(a).count("1") + bin(a).count("0"))


if __name__ == "__main__":
    input_array = [(100, 42),
                (20, 65515),
                (32000, 101),
                (42000, 42),
                (13, 12345),
                (9999, 9999),
                (8008, 37331),
                (54311, 2),
                (31200, 34335)]
    for input in input_array:
        print(score(input[0], input[1]))

