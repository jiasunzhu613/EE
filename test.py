
P = 27
M = 10**9 + 7

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
print(psa)

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())
    print(psa[r] - (psa[l - 1] * pow(P, r - l + 1)))
    print(get_hash(arr, l, r))
    print()


"""
5
1 2 3 4 5
8
1 2
1 1
2 2
5 5
2 4
2 3
4 5
1 5
"""


