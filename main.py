with open("data/data1.txt", "r") as inFile:
    N, Q = map(int, inFile.readline())
    arr = [0] + list(map(int, inFile.readline().split()))

