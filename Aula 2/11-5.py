def add_vectors(u, v):
    w = u[:]
    for i in range(len(u)):
        w[i] += v[i]
    return w

print(add_vectors([1, 1], [1, 1]) == [2, 2])
print(add_vectors([1, 2], [1, 4]) == [2, 6])
print(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])