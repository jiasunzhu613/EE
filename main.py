import random, math

# MODIFIED FENWICK FUNCTIONS
def LSB(i):
    return i & -i

#TODO: construct method causing overflow errors
def construct(arr): # where arr is a 1 indexed array of numbers
    fenwick = arr.copy()
    for i in range(1, len(fenwick)):
        lsb = LSB(i)
        j = i + lsb
        if j < len(fenwick):
            fenwick[j] += fenwick[i] * pow(P, lsb, M)
            fenwick[j] %= M
    return fenwick

def range_sum(fenwick, i):
    tot = 0
    lsb_counter = 0
    while i != 0:
        tot += fenwick[i]
        tot %= M
        i -= LSB(i)
    return tot

#TODO: problems caused by modding and dividing, once a number is modded it is no longer a direct multiple of P
def interval_sum(fenwick, i, j):
    #prolly shouldnt divide // pow(P, min(i, j) - 1)
    return ((range_sum(fenwick, j) - range_sum(fenwick, i - 1))// pow(P, min(i, j) - 1)) % M

def update(fenwick, ind, diff):
    while ind < len(fenwick):
        fenwick[ind] += diff
        fenwick[ind] %= M
        ind += LSB(ind)
    return

# SOLVE
P = 27
M = 10**9 + 7
N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
new_arr = arr.copy()
# for i in range(1, N + 1):
#     arr[i] *= pow(P, i - 1, M)
fenwick = construct(arr)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        print(fenwick)
        print(interval_sum(fenwick, query[1], query[2]))
        print(interval_sum(fenwick, query[3], query[4]))
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