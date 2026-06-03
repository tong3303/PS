def a(a, b, m):
    value = 1
    while b > 0:
        value = (a * value) % m
        b -= 1
    return value


def b(a, b, m):
    value = 1
    while b > 0:
        value *= a
        b -= 1
    return value % m


print(a(3, 7, 8))
print(b(3, 7, 8))