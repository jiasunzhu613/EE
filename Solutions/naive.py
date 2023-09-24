N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        l1, r1, l2, r2 = q[1:]
        out = 1
        for i in range(r1-l1 + 1):
            if arr[l1 + i] != arr[l2 + i]:
                out = 0
        print(out)
    else:
        i, v = q[1:]
        arr[i] = v