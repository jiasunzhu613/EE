import random

# MODIFIED FENWICK FUNCTIONS
def LSB(i):
    return i & -i

#TODO: construct method causing overflow errors
def construct(arr): # where arr is a 1 indexed array of numbers
    fenwick = arr.copy()
    for i in range(1, len(fenwick)):
        j = i + LSB(i)
        if j < len(fenwick):
            fenwick[j] += fenwick[i]
    return fenwick

def range_sum(fenwick, i):
    tot = 0
    while i != 0:
        tot += fenwick[i]
        i -= LSB(i)
    return tot

def interval_sum(fenwick, i, j):
    return ((range_sum(fenwick, j) - range_sum(fenwick, i - 1)) // pow(P, min(i, j) - 1)) % M

def update(fenwick, ind, diff):
    while ind < len(fenwick):
        fenwick[ind] += diff
        ind += LSB(ind)
    return

# SOLVE
P = 27
M = 10**9 + 7
N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
new_arr = arr.copy()
for i in range(1, N + 1):
    arr[i] *= pow(P, i, M)
fenwick = construct(arr)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        print(int(interval_sum(fenwick, query[1], query[2]) == interval_sum(fenwick, query[3], query[4])))
    else:
        update(fenwick, query[1], abs(query[2]*pow(P, query[1], M) - arr[query[1]]))
        arr[query[1]] = query[2]*pow(P, query[1], M)

# print(arr)
# print(fenwick)
# print(interval_sum(fenwick, 1, 1))
# print(interval_sum(fenwick, 3, 3))
# print(interval_sum(fenwick, 1, 2))
# print(interval_sum(fenwick, 3, 4))