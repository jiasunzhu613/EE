N, Q = map(int, input().split())
arr = [0] + list(map(int, input().split()))

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        l1, r1, l2, r2 = q[1:]
        print(int(arr[l1:r1 + 1] == arr[l2:r2 + 1]))
    else:
        i, v = q[1:]
        arr[i] = v
