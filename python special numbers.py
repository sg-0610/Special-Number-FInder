import time
import random


def is_prime_wheel(n):
    """Check if a number is prime using wheel factorization for small numbers and Miller-Rabin for large numbers."""
    if n < 104729:  # Use wheel factorization for smaller numbers
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    else:
        # Switch to Miller-Rabin for larger numbers
        return is_prime(n)


def power(x, y, p):
    """Compute (x^y) % p efficiently."""
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def miller_rabin_test(d, n):
    """Perform one iteration of the Miller-Rabin test for a given base."""
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


def is_prime(n, k=4):
    """Determine if n is a prime number using the Miller-Rabin primality test."""
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for _ in range(k):
        if not miller_rabin_test(d, n):
            return False
    return True


def generate_palindromes(min_limit, max_limit):
    """Generate palindromic numbers within the specified range."""
    # Single-digit palindromes
    for i in range(min_limit, min(max_limit, 10)):
        yield i

    # Multi-digit palindromes
    for length in range(2, len(str(max_limit)) + 1):
        start = 10 ** (length // 2 - 1)
        end = 10 ** (length // 2)

        for half in range(start, end):
            # Even-length palindrome
            even_palindrome = int(str(half) + str(half)[::-1])
            if even_palindrome > max_limit:
                return
            if even_palindrome >= min_limit:
                yield even_palindrome

            # Odd-length palindrome
            if length % 2 == 1:
                for middle in range(10):
                    odd_palindrome = int(str(half) + str(middle) + str(half)[::-1])
                    if odd_palindrome > max_limit:
                        break
                    if odd_palindrome >= min_limit:
                        yield odd_palindrome


def find_special_numbers(min_limit, max_limit):
    """Find special numbers that are both prime and palindromic."""
    special_numbers = [num for num in generate_palindromes(min_limit, max_limit) if is_prime_wheel(num)]
    count = len(special_numbers)

    print(f"There are {count} special numbers between {min_limit} and {max_limit}.")
    if count > 0:
        print("First three special numbers are:", special_numbers[:3])
        print("Last three special numbers are:", special_numbers[-3:])
    else:
        print("There are no special numbers in this range.")


if __name__ == "__main__":
    min_limit = int(input("Enter the smaller number (min_limit): "))
    max_limit = int(input("Enter the larger number (max_limit): "))
    start_time = time.time()
    find_special_numbers(min_limit, max_limit)
    end_time = time.time()
    print(f"Runtime: {end_time - start_time} seconds")