n, k = map(int, input().split())

def permutations(n, k):
    f = [False] * (n + 1)
    ans = []
    def gen(current):
        if len(current) == k:
            ans.append(current[:])
            return
        for i in range(1, n + 1):
            if not f[i]:
                f[i] = True
                current.append(i)
                gen(current)
                current.pop()
                f[i] = False

    gen([])
    ans.sort()

    for perm in ans:
        print(' '.join(map(str, perm)))

permutations(n, k)
