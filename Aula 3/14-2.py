import time,  random


def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.

def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1,len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False

def main(sz):
    rng = random.Random()   # Instantiate a generator

    bd = list(range(sz))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 1:
        rng.shuffle(bd)
        tries += 1
        if not has_clashes(bd):
           tries = 0
           num_found += 1
           print("Found solution {0} in {1} tries.".format(bd, tries))

main(4)
main(12)
main(16)

def max_in_a_minute():
    n = 4
    delta  = 0
    while delta < 60:
        rng = random.Random()  # Instantiate a generator
        bd = list(range(n))  # Generate the initial permutation
        found = False
        ini = time.clock()
        while not found and delta < 60:
            rng.shuffle(bd)
            if not has_clashes(bd):
                found = True
                n += 1
            delta = time.clock() - ini
    print("The biggest board that can be solved in a minute was {0}".format(n))

max_in_a_minute()