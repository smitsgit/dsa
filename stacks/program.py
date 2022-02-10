class Stack:
    def __init__(self):
        self._list = []

    def push(self, data):
        self._list.append(data)

    def pop(self):
        return self._list.pop()

    def is_empty(self):
        return len(self._list) == 0


def evaluate_postfix(expr):
    stack = Stack()
    for item in expr:
        if item.isdigit():
            stack.push(int(item))
        elif item in ['+', '-', '*', '/']:
            op1 = stack.pop()
            op2 = stack.pop()
            result = op1 + op2
            stack.push(result)
    result = stack.pop()
    print(result)


def check_parens(expr):
    stack = Stack()
    for item in expr:
        if item == '(':
            stack.push(item)
        elif item == ')':
            stack.pop()
        else:
            continue

    if stack.is_empty():
        return True
    else:
        return False


def main():
    expr = "((((10 + 23 + 45) - 10 * 30) + 2)"
    if check_parens(expr):
        print("Balanced")
    else:
        print("Unbalanced")

    postfix = "45+"
    evaluate_postfix(postfix)


if __name__ == '__main__':
    main()
