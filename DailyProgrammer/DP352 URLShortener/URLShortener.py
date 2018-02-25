class ShortenURL:
    BASE = 62
    ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def shorten(self, decimal_input):
        dividend = decimal_input
        divisor = self.BASE
        quotient = None
        output_stack = []

        while quotient != 0:
            quotient = dividend // divisor
            remainder = dividend % divisor
            output_stack.append(self.ALPHABET[remainder])
            dividend = quotient

        return ''.join(output_stack[::-1])


if __name__ == '__main__':
    examples = [15674, 7026425611433322325, 187621,
                237860461, 2187521, 18752,
                99999999999999999999]
    url = ShortenURL()
    for example in examples:
        print('{:<30} : {:<30}'.format(example, url.shorten(example)))
