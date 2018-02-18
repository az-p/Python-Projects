import re

ASCII_OFFSET_A_M = 65
ASCII_OFFSET_N_Z = 78
ASCII_OFFSET_a_m = 97
ASCII_OFFSET_n_z = 110
key = None


def main():
    global key
    key = read_key('key.txt')
    #key = read_key('test_key.txt')
    if key is None:
        print('Re-prompt user for key file')
        exit(1)
    print(decrypt_string('TpnQSjdmZdpoohd'))
    #print(decrypt_string('p'))
    #print(decrypt_string('T'))


def decrypt_string(st):
    decrypted_str = []
    for ltr in st:
        decrypted_str.append(solve_letter(ltr))
    return ''.join(decrypted_str)


# NAME:   read_key()
# DESC:   Gets index from ascii and searches for result
# IN:     key_file : File name [string]
# OUT:    arr : List of strings representing key [list]
def read_key(key_file):
    arr = []
    # Key may contain only space or slashes
    acceptable_chars = re.compile(r'^[ /\\]{13}')

    f = open(key_file, 'r')
    line_num = 0
    while line_num < 13:
        arr.append(f.readline().strip('\n'))
        # arr.append(f.readline())
        line_num += 1
    f.close()

    try:
        for a, val in enumerate(arr):
            if not acceptable_chars.match(val):
                raise ValueError('Bad characters found in key file at line: ', a)
            if len(val) != 13:
                raise ValueError('Too many characters in key file at line:', a)
    except ValueError as err:
        print(err.args)
        return None

    assert isinstance(arr, list)
    return arr


# NAME:   solve_letter()
# DESC:   Gets index from ascii and searches for result
# IN:     letter : Encrypted letter [string]
# OUT:    letter : Decrypted letter [string]
def solve_letter(letter):
    if 'A' <= letter <= 'M':
        # A to N is list index 0 to 13
        idx = ord(letter) - ASCII_OFFSET_A_M
        return search_key('r', 0, idx)
    elif 'n' <= letter <= 'z':
        # n to z is list index 0 to 13
        idx = ord(letter) - ASCII_OFFSET_n_z
        return search_key('l', 12, idx)
    elif 'N' <= letter <= 'Z':
        # N to Z is string index 0 to 13
        idx = ord(letter) - ASCII_OFFSET_N_Z
        return search_key('u', idx, 12)
    elif 'a' <= letter <= 'm':
        # a to m is string index 0 to 13
        idx = ord(letter) - ASCII_OFFSET_a_m
        return search_key('d', idx, 0)
    else:
        raise ValueError('Letter is invalid')


# NAME:   search_key()
# DESC:   Searches up/down/left/right (dir variable)
# IN:     dir = 'r', 'l', 'u', or 'd' : direction of search
#         x_start [int] : position in string for up/down search
#         y_start [int] : list index for left/right search
# OUT:    resLetter = alpha character encoded by letter
def search_key(dir, x_start, y_start):
    global key

    # Base cases (additional cases in lines after this block)
    if x_start < 0:
        # A-M
        return chr(y_start + ASCII_OFFSET_A_M)
    elif x_start > 12:
        # n-z
        return chr(y_start + ASCII_OFFSET_n_z)
    elif y_start < 0:
        # a-m
        return chr(x_start + ASCII_OFFSET_a_m)
    elif y_start > 12:
        # N-Z
        return chr(x_start + ASCII_OFFSET_N_Z)

    # TODO: Remove debug statement
    print_step(x_start, y_start)

    # Movement steps and base cases
    if dir == 'r':
        for i, val in enumerate(key[y_start]):
            print_step(i, y_start)
            if i >= x_start and val == '/':
                return search_key('u', i, y_start - 1)
            elif i >= x_start and val == '\\':
                return search_key('d', i, y_start + 1)
        # n-z
        return chr(y_start + ASCII_OFFSET_n_z)

    if dir == 'l':
        for i, val in reversed(list(enumerate(key[y_start]))):
            print_step(i, y_start)
            if i <= x_start and val == '/':
                return search_key('d', i, y_start + 1)
            elif i <= x_start and val == '\\':
                return search_key('u', i, y_start - 1)
        # A-M
        return chr(y_start + ASCII_OFFSET_A_M)

    if dir == 'u':
        for i, val in reversed(list(enumerate(key))):
            print_step(x_start, i)
            if i <= y_start and val[x_start] == '/':
                return search_key('r', x_start + 1, i)
            elif i <= y_start and val[x_start] == '\\':
                return search_key('l', x_start - 1, i)
        # a-m
        return chr(x_start + ASCII_OFFSET_a_m)

    if dir == 'd':
        for i, val in enumerate(key):
            print_step(x_start, i)
            if i >= y_start and val[x_start] == '/':
                return search_key('l', x_start - 1, i)
            elif i >= y_start and val[x_start] == '\\':
                return search_key('r', x_start + 1, i)
        # N-Z
        return chr(x_start + ASCII_OFFSET_N_Z)


def print_step(x, y):
    global key

    for i, val in enumerate(key):
        if y == i:
            print(val[:x], '*', val[x+1:], sep='')
        else:
            print(val)
    print('-'*13)
if __name__ == '__main__':
    main()
