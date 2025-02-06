#first check if the number is prime
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisibility from 2 to the square root of n
        if n % i == 0:
            return False  # Found a divisor, not a prime
    return True  # No divisors found, it's prime
print(is_prime(8))
