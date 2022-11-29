# Method 1


def m1():
    s = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            s = s + i

    return s


# Method 2
def m2():
    s2 = sum(range(3, 1000, 3)) + sum(range(5, 1000, 5)) - sum(range(15, 1000, 15))

    return s2
