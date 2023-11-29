class Polynomial_hash:
    def __int__(self, arr, N):
        self.arr = arr
        self.N = N
        self.P = 209389283097
        self.M = 10 ** 9 + 7
        self.prefix_hash = self.construct(arr)

    def construct(self, arr):
        prefix_hash = []
        hash = 0
        for i in range(N + 1):
            hash *= P
            hash += arr[i]
            hash %= M
            prefix_hash.append(hash)
        return prefix_hash

    def query(self, prefix_hash, l, r):
        return (prefix_hash[r] - (prefix_hash[l - 1] * pow(P, r-l+1, M))) % M

    def update(self, pos, val):
        for j in range(i, N + 1):
            replacement = v * pow(P, j - i, M) - arr[i] * pow(P, j - i, M)
            self.prefix_hash[j] += replacement
            self.prefix_hash[j] %= M
        self.arr[i] = v
        return




