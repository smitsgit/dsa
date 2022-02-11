class Tokenizer:
    def __init__(self, expr):
        self.expr = expr
        self.position = -1
        self.read_position = self.position + 1
        self.chr = None

    def read_char(self):
        if self.read_position < len(self.expr):
            self.chr = self.expr[self.read_position]
        else:
            self.chr = 0
        self.position = self.read_position
        self.read_position += 1

    def next_token(self):
        tok = None
        if self.read_position > len(self.expr):
            return tok
        self.skip_none()
        self.skip_whitespace()

        if self.chr == '+':
            tok = self.chr
        else:
            if self.chr.isdigit():
                num = self.read_num()
                tok = num
        self.read_char()
        return tok

    def skip_none(self):
        while self.chr is None:
            self.read_char()

    def skip_whitespace(self):
        while self.chr in [' ', '\t', '\r']:
            self.read_char()

    def read_num(self):
        position = self.position
        while True:
            if self.read_position > len(self.expr):
                tok = None
                break
            if self.chr.isdigit():
                self.read_char()
                continue
            else:
                break
        return self.expr[position: self.position]

    def __iter__(self):
        return self

    def __next__(self):
        tok = self.next_token()
        if tok is None:
            raise StopIteration()
        else:
            return tok


def main():
    expr = "123 + 425"
    tokenizer = Tokenizer(expr)
    for item in tokenizer:
        print(item)


if __name__ == '__main__':
    main()
