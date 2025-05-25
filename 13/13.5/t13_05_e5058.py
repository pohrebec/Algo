sequence = input()

def balanced(s: str) -> str:
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack:
                return "no"
            top_element = stack.pop()
            if mapping[char] != top_element:
                return "no"
    return "yes" if not stack else "no"

print(balanced(sequence))