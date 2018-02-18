def test_input():
    writeCheck(333.88)
    writeCheck(742388.15)
    writeCheck(919616.12)
    writeCheck(12.11)
    writeCheck(2.0)


def write_check(amt):
    ones = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
        }
    hundreds = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }

    txtAmt = chr(amt).split('.')
    dollars, cents = txtAmt[0], txtAmt[1]

    # Divide by 3 to get hundred, thousand, etc
    # Standard interpretation of each chunk of three

if __name__ == '__main__':
    testInput()
