from typing import Any

def _ensure_int(n: Any) -> int:
    if not isinstance(n, int):
        raise TypeError("Expected an integer")
    return n

def square(n: Any) -> int:
    n = _ensure_int(n)
    return n * n

def factorial(n: Any) -> int:
    n = _ensure_int(n)
    if n < 0:
        raise ValueError("Factorial is undefined for negative integers")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

def is_prime(n: Any) -> bool:
    n = _ensure_int(n)
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    k = 3
    while k * k <= n:
        if n % k == 0:
            return False
        k += 2
    return True

def gcd(a: Any, b: Any) -> int:
    a = _ensure_int(a)
    b = _ensure_int(b)
    while b != 0:
        a, b = b, a % b
    return abs(a)

def lcm(a: Any, b: Any) -> int:
    a = _ensure_int(a)
    b = _ensure_int(b)
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)
