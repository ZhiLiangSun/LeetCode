def solve(A, B, M, X, Y):
    if len(A) != len(B):
        return 0

    length = len(A)
    i = 0
    stops = 0
    while i < length:
        group_weight = 0.0
        cap = 0
        unique_floors = {}

        if B[i] > M:
            del B[i], A[i]
            length = len(A)
            continue

        while cap < X and i < length and (group_weight + A[i]) <= Y and B[i] <= M:
            group_weight = group_weight + A[i]
            unique_floors[B[i]] = i
            i = i + 1
            cap = cap + 1
        stops = stops + len(unique_floors) + 1
    return stops


A = [60, 80, 40]
B = [2, 3, 5]
M = 5
X = 2
Y = 200
print(solve(A, B, M, X, Y))

A = [40, 40, 100, 80, 20]
B = [3, 3, 2, 2, 3]
M = 3
X = 5
Y = 200
print(solve(A, B, M, X, Y))

A = [40, 40, 100, 200, 20]
B = [3, 3, 2, 2, 3]
M = 3
X = 5
Y = 200
print(solve(A, B, M, X, Y))

A = [40, 40, 100, 200, 20]
B = [3, 3, 2, 2, 3]
M = 3
X = 1
Y = 200
print(solve(A, B, M, X, Y))

A = [40, 40, 100, 200, 20]
B = [3, 3, 2, 2, 5]
M = 3
X = 1
Y = 200
print(solve(A, B, M, X, Y))

A = [40, 40, 100, 200, 20]
B = [3, 3, 5, 2, 2]
M = 3
X = 1
Y = 200
print(solve(A, B, M, X, Y))

A = [40, 40, 100, 200, 20]
B = [3, 2, 3, 5, 2]
M = 3
X = 5
Y = 200
print(solve(A, B, M, X, Y))
