BRACKET_ROUND_OPEN = '('
BRACKET_ROUND__CLOSE = ')'
BRACKET_CURLY_OPEN = '{'
BRACKET_CURLY_CLOSE = '}'
BRACKET_SQUARE_OPEN = '['
BRACKET_SQUARE_CLOSE = ']'

TUPLE_OPEN_CLOSE = [(BRACKET_ROUND_OPEN,BRACKET_ROUND__CLOSE),
                    (BRACKET_CURLY_OPEN,BRACKET_CURLY_CLOSE),
                    (BRACKET_SQUARE_OPEN,BRACKET_SQUARE_CLOSE)]
BRACKET_LIST = [BRACKET_ROUND_OPEN,BRACKET_ROUND__CLOSE,BRACKET_CURLY_OPEN,BRACKET_CURLY_CLOSE,BRACKET_SQUARE_OPEN,BRACKET_SQUARE_CLOSE]

def balanced_parentheses(expression):
    stack = list()
    left = expression[0]
    for exp in expression:
        if exp not in BRACKET_LIST:
            continue
        skip = False
        for bracket_couple in TUPLE_OPEN_CLOSE:
            if exp != bracket_couple[0] and exp != bracket_couple[1]:
                continue
            if left == bracket_couple[0] and exp == bracket_couple[1]:
                if len(stack) == 0:
                    return False
                stack.pop()
                skip = True
                left = ''
                if len(stack) > 0:
                    left = stack[len(stack) - 1]
        if not skip:
            left = exp
            stack.append(exp)

    return len(stack) == 0
if __name__ == '__main__':
	print(balanced_parentheses('(()())({})[]'))#True
    print(balanced_parentheses('((ali)(koyuncu))({})[]'))#True
    print(balanced_parentheses('(()())())'))#False