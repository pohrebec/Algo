import sys

degree = 10
size = degree + 1

def zero():
    return [0] * size

def const(value):
    poly = zero()
    poly[0] = value
    return poly

def n():
    poly = zero()
    poly[1] = 1
    return poly

def add_polynom(poly1, poly2):
    result = zero()
    for i in range(size):
        result[i] = poly1[i] + poly2[i]
    return result

def multiply_polynom(poly1, poly2):
    result = zero()
    for i in range(size):
        for j in range(size):
            if i + j < size:
                result[i + j] += poly1[i] * poly2[j]
    return result

def format(poly):
    terms = []
    for i in range(degree, -1, -1):
        coef = poly[i]
        if coef == 0:
            continue
        if i == 0:
            terms.append(str(coef))
        elif i == 1:
            if coef == 1:
                terms.append("n")
            else:
                terms.append(f"{coef}*n")
        else:
            if coef == 1:
                terms.append(f"n^{i}")
            else:
                terms.append(f"{coef}*n^{i}")
    if not terms:
        return "0"

    output = "+".join(terms)
    return output.replace("+-", "-")

def solve():
    full_input = sys.stdin.read()
    cleaned_input = full_input.replace('\n', ' ').split()
    num_programs = int(cleaned_input[0])
    token_index = 1

    for program_num in range(1, num_programs + 1):
        total_runtime = zero()
        current_multiplier_poly = const(1)
        multiplier_stack = []

        while cleaned_input[token_index] != "BEGIN":
            token_index += 1
        token_index += 1
        nesting_level = 1

        while True:
            token = cleaned_input[token_index]
            token_index += 1

            if token == "END":
                if nesting_level == 1:
                    break
                else:
                    nesting_level -= 1
                    current_multiplier_poly = multiplier_stack.pop()
            elif token == "LOOP":
                loop_param = cleaned_input[token_index]
                token_index += 1
                loop_multiplier = None

                if loop_param == "n":
                    loop_multiplier = n()
                else:
                    loop_multiplier = const(int(loop_param))

                multiplier_stack.append(current_multiplier_poly)
                current_multiplier_poly = multiply_polynom(current_multiplier_poly, loop_multiplier)
                nesting_level += 1

            elif token == "OP":
                op_value = int(cleaned_input[token_index])
                token_index += 1
                op_time_poly = const(op_value)
                term_to_add = multiply_polynom(op_time_poly, current_multiplier_poly)
                total_runtime = add_polynom(total_runtime, term_to_add)

        print(f"Program #{program_num}")
        print(f"Runtime = {format(total_runtime)}")

        if program_num < num_programs:
            print()

solve()
