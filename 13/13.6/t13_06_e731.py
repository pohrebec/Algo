prefix = input()

def prefix_infix(prefix_expr: str) -> str:
    stack = []
    op = set(['+', '-', '*', '/'])
    priorities = {'+': 1, '-': 1, '*': 2, '/': 2}

    for i in range(len(prefix_expr) - 1, -1, -1):
        char = prefix_expr[i]

        if char not in op:
            stack.append((char, 3))
        else:
            op_priority = priorities[char]

            left_str, left_priority = stack.pop()
            right_str, right_priority = stack.pop()

            if left_priority < op_priority:
                left_str = f"({left_str})"

            if right_priority < op_priority or \
                    (right_priority == op_priority and char in ['-', '/']):
                right_str = f"({right_str})"

            new_infix = f"{left_str}{char}{right_str}"
            stack.append((new_infix, op_priority))

    return stack[0][0]

print(prefix_infix(prefix))