class Naive:
    def __init__(self, arr, N):
        self.arr = arr
        self.N = N

    def query(self, l, r):
        return self.arr[l:r + 1]

    def update(self, pos, val):
        self.arr[pos] = val
        return














