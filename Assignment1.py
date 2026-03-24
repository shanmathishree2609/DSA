def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))

        else:
            if token == '!':   # unary operator
                a = stack.pop()
                stack.append(0 if a else 1)

            else:
                b = stack.pop()
                a = stack.pop()

                # Arithmetic
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a // b)

                # Comparison
                elif token == '<':
                    stack.append(1 if a < b else 0)
                elif token == '>':
                    stack.append(1 if a > b else 0)
                elif token == '<=':
                    stack.append(1 if a <= b else 0)
                elif token == '>=':
                    stack.append(1 if a >= b else 0)
                elif token == '==':
                    stack.append(1 if a == b else 0)
                elif token == '!=':
                    stack.append(1 if a != b else 0)

                # Logical
                elif token == '&&':
                    stack.append(1 if (a and b) else 0)
                elif token == '||':
                    stack.append(1 if (a or b) else 0)

    return stack.pop()


# Example expressions
expr1 = "2 3 * 5 4 * + 9 -"          # arithmetic
expr2 = "5 3 >"                      # comparison
expr3 = "5 3 > 2 1 > &&"             # logical

print("Arithmetic Result:", evaluate_postfix(expr1))
print("Comparison Result:", evaluate_postfix(expr2))
print("Logical Result:", evaluate_postfix(expr3))



def evaluate_prefix(expression):
    stack = []

    tokens = expression.split()[::-1]

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))

        else:
            if token == '!':   # unary operator
                a = stack.pop()
                stack.append(0 if a else 1)

            else:
                a = stack.pop()
                b = stack.pop()

                # Arithmetic
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a // b)

                # Comparison
                elif token == '<':
                    stack.append(1 if a < b else 0)
                elif token == '>':
                    stack.append(1 if a > b else 0)
                elif token == '<=':
                    stack.append(1 if a <= b else 0)
                elif token == '>=':
                    stack.append(1 if a >= b else 0)
                elif token == '==':
                    stack.append(1 if a == b else 0)
                elif token == '!=':
                    stack.append(1 if a != b else 0)

                # Logical
                elif token == '&&':
                    stack.append(1 if (a and b) else 0)
                elif token == '||':
                    stack.append(1 if (a or b) else 0)

    return stack.pop()


# Examples
expr1 = "- + * 2 3 * 5 4 9"     # arithmetic
expr2 = "> 5 3"                 # comparison
expr3 = "&& > 5 3 > 2 1"        # logical

print("Arithmetic Result:", evaluate_prefix(expr1))
print("Comparison Result:", evaluate_prefix(expr2))
print("Logical Result:", evaluate_prefix(expr3))
