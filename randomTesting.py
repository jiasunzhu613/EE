import random, math

# MODIFIED FENWICK FUNCTIONS
def LSB(i):
    return i & -i

#TODO: construct method causing overflow errors
def construct(arr): # where arr is a 1 indexed array of numbers
    fenwick = arr.copy()
    for i in range(1, len(fenwick)):
        j = i + LSB(i)
        if j < len(fenwick):
            fenwick[j] += fenwick[i] % M
    return fenwick

def range_sum(fenwick, i):
    tot = 0
    while i != 0:
        tot += fenwick[i] % M
        i -= LSB(i)
    return tot

#TODO: problems caused by modding and dividing, once a number is modded it is no longer a direct multiple of P
def interval_sum(fenwick, i, j):
    #// pow(P, min(i, j) - 1)
    return ((range_sum(fenwick, j) - range_sum(fenwick, i - 1))// pow(P, min(i, j) - 1)) % M

def update(fenwick, ind, diff):
    while ind < len(fenwick):
        fenwick[ind] += diff % M
        ind += LSB(ind)
    return


# SOLVE
P = 27
M = 10**9+7
for _ in range(100):
    N, Q = 10, random.randint(5, 10)
    arr = [0] + [random.randint(1, 10) for i in range(N)]
    new_arr = arr.copy()
    for i in range(1, N + 1):
        arr[i] *= pow(P, i - 1, M)
    fenwick = construct(arr)

    for _ in range(Q):
        type = random.randint(1, 3)
        if type == 1:
            a = random.randint(1, N - 1)
            b = random.randint(a, N)
            c = random.randint(1, N - 1)
            d = random.randint(c, N)
            def slow():
                return new_arr[a:b + 1] == new_arr[c:d+1]
            def fast():
                return interval_sum(fenwick, a, b) == interval_sum(fenwick, c, d)
            if slow() != fast():
                print(slow(), fast())
                print(*new_arr[1:])
                print(a, b, c, d)
                print()
        else:
            a = random.randint(1, N)
            b = random.randint(1, 10)
            update(fenwick, a, abs(b*pow(P, a, M) - arr[a]))
            arr[a] = b*pow(P, a, M)
            new_arr[a] = b
