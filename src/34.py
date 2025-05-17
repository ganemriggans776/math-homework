import numpy as np

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_primes(n):
    primes_sum = 0
    for num in range(2, n + 1):
        if is_prime(num):
            primes_sum += num
    return primes_sum

# Example usage
n = 50
print("The sum of all prime numbers up to", n, "is:", sum_of_primes(n))
