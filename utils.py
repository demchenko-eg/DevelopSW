from math import factorial as f

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def pow5(n):
    while n >= 5:
        if n % 5 != 0:
            return False
        n //= 5
    return True

def pow2(n):
    while n >= 2:
        if n % 2 != 0:
            return False
        n //= 2
    return True