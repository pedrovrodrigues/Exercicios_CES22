def is_factor(a,b):
    # test if a is a factor of b
    return b%a == 0

def is_multiple(a,b):
    # test if a is a factor of b
    return is_factor(b,a)

print(is_multiple(12, 3))
print(is_multiple(12, 4))
print(is_multiple(12, 5))
print(is_multiple(12, 6))
print(is_multiple(12, 7))
print(is_multiple(12, 1))
print(is_multiple(12, 12))

