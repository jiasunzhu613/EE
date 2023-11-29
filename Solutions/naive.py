class Naive:
    def __init__(self, arr, N):
        self.arr = arr
        self.N = N

    def query(self, arr, l, r):
        return arr[l:r + 1]

    def update(self, pos, val):
        self.arr[pos] = val
        return














