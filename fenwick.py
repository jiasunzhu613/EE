# NORMAL FENWICK FUNCTIONS
def LSB(i):
    return i & -i

def construct(arr): # where arr is a 1 indexed array of numbers
    N = len(arr)
    fenwick = arr.copy()
    for i in range(1, N):
        j = i + LSB(i)
        if j < N:
            fenwick[j] += i
    return fenwick

def range_sum(fenwick, i):
    tot = 0
    while i != 0:
        tot += fenwick[i]
        i -= LSB(i)
    return tot

def interval_sum(fenwick, i, j):
    return range_sum(fenwick, j) - range_sum(fenwick, i - 1)

def update(fenwick, ind, diff):
    while ind < len(fenwick):
        fenwick[ind] += diff
        ind += LSB(ind)