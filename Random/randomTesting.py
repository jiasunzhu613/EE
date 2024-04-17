import random, math

# Fenwick implementation
def LSB(x):
    return x & -x

def construct(arr):
    fenwick = arr.copy()
    for i in range(1, len(fenwick)):
        j = i + LSB(i)
        if j < len(fenwick):
            fenwick[j] += (fenwick[i] * pow(P, LSB(i), M)) % M
            fenwick[j] %= M
    return fenwick

def prefix_sum(fenwick, pos):
    tot = 0
    iteration = 0
    while pos > 0:
        tot += (fenwick[pos] * pow(P, iteration, M)) % M # might need mod after
        tot %= M
        iteration += LSB(pos)
        pos -= LSB(pos)
    return tot

# prefix_sum(r) - prefix_sum(l) - prefix_sum(l - 1)* pow(P, r-l+1) % M
def query(fenwick, l ,r):
    global P, M
    return (prefix_sum(fenwick, r) - prefix_sum(fenwick, l - 1) * pow(P, r-l+1, M)) % M
# * (pow(P, r - l + 1) + 1)

def update(fenwick, pos, diff):
    iteration = 0
    while pos < len(fenwick):
        fenwick[pos] += (diff * pow(P, iteration, M)) % M
        fenwick[pos] %= M
        iteration += LSB(pos)
        pos += LSB(pos)
    return


# SOLVE
P = 27
M = 10**9+7
for _ in range(100):
    N, Q = 10, random.randint(5, 10)
    arr = [0] + [random.randint(1, 10) for i in range(N)]
    pre_change = arr.copy()
    updates = []
    fenwick = construct(arr)

    for _ in range(Q):
        type = random.randint(1, 2)
        if type == 1:
            length = random.randint(1, 9)
            a = random.randint(1, N - length)
            b = a + length
            c = random.randint(1, N - length)
            d = c + length
            def slow():
                return arr[a:b + 1] == arr[c:d+1]
            def fast():
                return query(fenwick, a, b) == query(fenwick, c, d)
            if slow() != fast():
                print(slow(), fast())
                print(*pre_change[1:])
                print(a, b, c, d)
                for i in updates:
                    print(*i)
                print()
        else:
            a = random.randint(1, N)
            b = random.randint(1, 10)
            updates.append((a, b))
            update(fenwick, a, b - arr[a])
            arr[a] = b
