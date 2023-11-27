from functools import reduce

def product_modulo(a, b):
    return (a * b) % 10**6

def cunr(n):
    return reduce(product_modulo, range(2*n-5, 1, -2))

n = 840

result = cunr(n)
print(result)

