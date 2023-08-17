P = 27
M = 10**9 + 7

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

def get_hash(arr, l, r):
    hash = 0
    for i in range(l, r + 1):
        hash %= M
        hash *= P
        hash += arr[i]
        hash %= M
    return hash

N = int(input())
arr = [0] + list(map(int, input().split()))
psa = []

# precompute hashes into psa
# using precomputed hashes, we can use psa[r] - psa[l] * pow(P, r - l + 1)
# to compute the hash of substring from index l to r inclusive
hash = 0
for i in range(N + 1):
    hash %= M
    hash *= P
    hash += arr[i]
    hash %= M
    psa.append(hash)

fenwick = construct(arr)
print(fenwick)
# update(fenwick, 7, 7 - 10)
# update(fenwick, 6, 6 - 10)
# should look like -> [0, 1, 29, 3, 21226, 5]
print(psa)

# for i in range(1, 10 + 1):
#     print(i)
#     print(query(fenwick, 1, i))
#     print(get_hash(arr, 1, i))
#     print()

# print(prefix_sum(fenwick, 4))
# print(prefix_sum(fenwick, 1))
# print(get_hash(arr, 1, 4))
Q = int(input())
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        l, r, ll, rr = q[1:]
        print(query(fenwick, l, r))
        print(get_hash(arr, l, r))
        print(query(fenwick, ll, rr))
        print(get_hash(arr, ll, rr))
        print(query(fenwick, l, r) == query(fenwick, ll, rr))
        print()
    else:
        i, v = q[1:]
        update(fenwick, i, v - arr[i])
        arr[i] = v
        for i in range(1, 10 + 1):
            print(i)
            print(query(fenwick, 1, i))
            print(get_hash(arr, 1, i))
            print()



    # l, r = map(int, input().split())
    # print((psa[r] - (psa[l - 1] * pow(P, r - l + 1))) % M)


"""
10
1 2 3 4 5 6 7 8 9 10
3
1 8
1 10
1 7
5
1 2 3 2 5
8
1 2
1 3
2 2
4 4
5 5
2 4
2 3
4 5
1 5

10
5 5 5 7 7 7 8 5000000 8 5000000
2
8 8 
10 10

True False
10 
7 9 7 10 7 1 3 7 8 5
2
1 1 
8 8

True False
10 
6 6 8 4 6 4 1 6 8 5
2
2 2 
8 8

True False
10
1 6 8 1 7 3 2 1 5 5
5
2 7 2
2 6 3
2 2 6
1 8 8
1 1 1

1 8 8 1 1

False True
10
8 9 1 2 7 8 4 4 1 2
6
2 6 2
2 6 8
2 1 8
2 3 1
1 8 8 3 3

False True
10
9 7 10 7 1 9 1 2 3 8
2
2 10 8
1 10 10 3 3

True False
10
5 2 4 7 10 1 10 10 4 6
2
2 8 10
1 8 8 5 5



False True
10
2 1 4 1 7 10 2 2 6 1
9 6
2 1
9 10 4 4

False True
1 3 1 10 6 3 6 5 4 2
9 9 10 10
9 4

False True
10 1 7 8 6 5 8 10 9 10
4 9 5 9
2 1
4 10
4 8
3 7

True False
10
9 8 9 8 9 9 6 8 10 9
5
2 7 6
2 2 8
2 4 8
2 9 10
1 2 3 4 5

after change: 9 8 9 8 9 9 6 8 10 9

10
4 9 3 2 1 5 4 1 3 2
4
2 3 10
2 3 3
2 6 7
1 5 6 8 9

after change: 4 9 3 2 1 7 4 1 3 2
"""


