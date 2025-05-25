from collections import deque

n = int(input())
first_cards = list(map(int, input().split()))
second_cards = list(map(int, input().split()))

def game(n, first_cards, second_cards):
    first = deque(first_cards)
    second = deque(second_cards)
    max_steps = 2 * 10 ** 5
    steps = 0

    while first and second and steps < max_steps:
        a = first.popleft()
        b = second.popleft()
        if (a > b and not (a == n - 1 and b == 0)) or (a == 0 and b == n - 1):
            first.append(a)
            first.append(b)
        else:
            second.append(a)
            second.append(b)
        steps += 1

    if not first:
        print("second", steps)
    elif not second:
        print("first", steps)
    else:
        print("draw")

game(n, first_cards, second_cards)
