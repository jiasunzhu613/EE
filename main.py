from timeit import default_timer as timer
from Solutions.naive import Naive
from Solutions.polynomial_hash import Polynomial_hash
from Solutions.bit_and_polynomial_hashing import BIT_and_polynomial_hashing

with open("data/data1.txt", "r") as inFile:
    N, Q = map(int, inFile.readline().split())
    arr = [0] + list(map(int, inFile.readline().split()))

    naive_sol = Naive(arr, N)
    polynomial_hashing_sol = Polynomial_hash(arr, N)
    BIT_hashing_sol = BIT_and_polynomial_hashing(arr, N)

    queries = []
    for _ in range(Q):
        queries.append(list(map(int, inFile.readline().split())))



    # polyhash_start = timer()
    # for query in queries:
    #     if query[0] == 1:
    #         t, l1, r1, l2, r2 = query
    #         polynomial_hashing_sol.query(l1, r1)
    #         polynomial_hashing_sol.query(l2, r2)
    #     if query[0] == 2:
    #         t, ind, val = query
    #         polynomial_hashing_sol.update(ind, val)
    # polyhash_end = timer()
    # print(f"PolyHashing Solution took: {polyhash_end - polyhash_start}")

    bit_polyhash_start = timer()
    for query in queries:
        if query[0] == 1:
            t, l1, r1, l2, r2 = query
            BIT_hashing_sol.query(l1, r1)
            BIT_hashing_sol.query(l2, r2)
        if query[0] == 2:
            t, ind, val = query
            BIT_hashing_sol.update(ind, val)
    bit_polyhash_end = timer()
    print(f"BIT & Hashing Solution took: {bit_polyhash_end - bit_polyhash_start}")

    naive_start = timer()
    for query in queries:
        if query[0] == 1:
            t, l1, r1, l2, r2 = query
            naive_sol.query(l1, r1)
            naive_sol.query(l2, r2)
        if query[0] == 2:
            t, ind, val = query
            naive_sol.update(ind, val)
    naive_end = timer()
    print(f"Naive Solution took: {naive_end - naive_start}")

