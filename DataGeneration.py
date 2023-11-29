import random
# TODO:
# - write cases with changing elements
# - write cases without chanding elements
# with changing elements
MAX = 10**9
Q_N_MAX = 5 * 10**5
with open("data/data1.txt", "w") as outFile:
    # N, Q = random.randint(1, Q_N_MAX), random.randint(1, Q_N_MAX)
    N, Q = Q_N_MAX, Q_N_MAX
    outFile.write(f"{N} {Q}\n")
    arr = [random.randint(1, MAX) for i in range(N)]
    outFile.write(" ".join(list(map(str, arr))) + "\n")

    for _ in range(Q):
        typeOfQuery = random.randint(1, 2)
        if typeOfQuery == 1:
            length = random.randint(1, N)
            l1 = random.randint(1, N - length)
            r1 = l1 + length
            l2 = random.randint(1, N - length)
            r2 = l2 + length
            outFile.write(f"{typeOfQuery} {l1} {r1} {l2} {r2}\n")
        else:
            ind = random.randint(1, N)
            val = random.randint(1, MAX)
            outFile.write(f"{typeOfQuery} {ind} {val}\n")
    outFile.close()



