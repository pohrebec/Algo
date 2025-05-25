def permutation(target, n):
    stack = []
    curr = 1
    for num in target:
        while curr <= n and (not stack or stack[-1] != num):
            stack.append(curr)
            curr += 1
        if stack[-1] == num:
            stack.pop()
        else:
            return False
    return True

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        while True:
            line = input()
            if line == "0":
                break
            target = list(map(int, line.strip().split()))
            if permutation(target, n):
                print("Yes")
            else:
                print("No")

if __name__ == "__main__":
    main()
