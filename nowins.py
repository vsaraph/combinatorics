import itertools

# does there exist an element it fixes
def not_derange(perm):
    n = len(perm)
    for i in range(n):
        if perm[i] == i:
            return True
    return False

# does there exist an element sent to its "opposite"
def not_anti_derange(perm):
    n = len(perm)
    for i in range(n):
        if perm[i] == n - i - 1:
            return True
    return False

# over all naturals
n = 1
while True:
    # over all permutations of n
    count = 0
    for perm in itertools.permutations(range(n)):
        if not_derange(perm) and not_anti_derange(perm):
            count += 1
    print("%d: %d" % (n, count))
    n += 1
