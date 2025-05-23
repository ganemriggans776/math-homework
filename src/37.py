def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            return False
        i += 2
    return True

def prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0 and is_prime(i):
            factors.append(int(i))
            n //= i
        else:
            i += 1
    return factors

# Example usage
print(prime_factors(36)) # Output: [2, 2, 3, 3]
