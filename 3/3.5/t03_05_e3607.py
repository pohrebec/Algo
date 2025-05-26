import sys

def linear():
    input_lines = sys.stdin.read().strip().split('\n')
    i = 0
    while i < len(input_lines):
        n = int(input_lines[i])
        i += 1
        heights = list(map(int, input_lines[i].split()))
        i += 1
        a, b = map(int, input_lines[i].split())
        i += 1
        count = 0

        for h in heights:
            if a <= h <= b:
                count += 1
        print(count)

linear()
