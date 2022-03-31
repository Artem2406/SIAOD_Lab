import Num1


def check_square_brackets(string):
    bracket_stack = Num1.Deque()
    for i in string:
        if i == '[':
            bracket_stack.push(i)
        elif i == ']':
            if bracket_stack.is_empty():
                return False
            bracket_stack.pop()
    return bracket_stack.is_empty()
print(check_square_brackets('[[[]]'))
print(check_square_brackets('[[][][]]'))