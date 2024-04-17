P = 209389283097
M = 10**9 + 7
class Polynomial_hash:
    def __init__(self, arr, N):
        self.arr = arr
        self.N = N
        self.prefix_hash = self.construct(arr)

    def construct(self, arr):
        prefix_hash = []
        hash = 0
        for i in range(self.N + 1):
            hash *= P
            hash += arr[i]
            hash %= M
            prefix_hash.append(hash)
        return prefix_hash

    def query(self, l, r):
        return (self.prefix_hash[r] - (self.prefix_hash[l - 1] * pow(P, r-l+1, M))) % M

    def update(self, pos, val):
        for j in range(pos, self.N + 1):
            replacement = val * pow(P, j - pos, M) - self.arr[pos] * pow(P, j - pos, M)
            self.prefix_hash[j] += replacement
            self.prefix_hash[j] %= M
        self.arr[pos] = val
        return




