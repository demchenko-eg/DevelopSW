from math import factorial as f

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def pow5(n):
    while n >= 5:
        if n % 5 != 0:
            return False
        n //= 5
    return True