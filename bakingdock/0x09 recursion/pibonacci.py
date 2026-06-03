def pibonacci(n):
    if n <= 2:
        return 1
    else:
        return pibonacci(n-1) + pibonacci(n-2)

# result = pibonacci(6)
# print(result)

# -------------------------------------------------------------------------------------------------------------
def pibonacci2(n):
    a, b = 1, 1
    sum = 0
    for i in range(n):
        if i <= 1:
            result = 1
            sum += 1
        else:
            a, b = b, a + b
            result = b
            sum += b

        print(result, end=" ")
    return sum

result1 = pibonacci2(6)
print("\nsum = ", result1)



