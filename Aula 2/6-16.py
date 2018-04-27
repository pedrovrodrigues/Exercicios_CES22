def is_factor(a,b):
    # test if a is a factor of b
    return b%a == 0

print(is_factor( 3,12))
print(is_factor( 5,12))
print(is_factor( 7,14))
print(is_factor( 7,15))
print(is_factor( 1,15))
print(is_factor(15,15))
print(is_factor(25,15))
