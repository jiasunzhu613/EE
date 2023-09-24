P = 209389283097
M = 10**9 + 7

N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))

prefix_hash = []
hash = 0
for i in range(N + 1):
    hash *= P
    hash += arr[i]
    hash %= M
    prefix_hash.append(hash)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        l1, r1, l2, r2 = q[1:]
        # pow() has log factor from binary exponentiation
        print(int((prefix_hash[r1] - (prefix_hash[l1 - 1] * pow(P, r1-l1+1, M)))%M == (prefix_hash[r2] - (prefix_hash[l2 - 1]* pow(P, r2-l2+1, M)))%M))
    else:
        i, v = q[1:]
        for j in range(i, N + 1):
            replacement = v * pow(P, j - i, M) - arr[i] * pow(P, j - i, M)
            prefix_hash[j] += replacement
            prefix_hash[j] %= M
        arr[i] = v
