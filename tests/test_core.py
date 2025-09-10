import pytest
from mathutils import square, factorial, is_prime, gcd, lcm

# --- square ---
def test_square_happy_positive():
    assert square(5) == 25

def test_square_happy_negative():
    assert square(-4) == 16

def test_square_type_error():
    with pytest.raises(TypeError):
        square(3.14)

# --- factorial ---
def test_factorial_happy_small():
    assert factorial(5) == 120

def test_factorial_happy_zero():
    assert factorial(0) == 1

def test_factorial_negative_error():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_type_error():
    with pytest.raises(TypeError):
        factorial("6")

# --- is_prime ---
def test_is_prime_happy_prime():
    assert is_prime(13) is True

def test_is_prime_happy_composite():
    assert is_prime(21) is False

def test_is_prime_edge_less_than_2():
    assert is_prime(1) is False
    assert is_prime(0) is False

def test_is_prime_type_error():
    with pytest.raises(TypeError):
        is_prime(2.0)

# --- gcd ---
def test_gcd_happy_basic():
    assert gcd(54, 24) == 6

def test_gcd_happy_with_negatives():
    assert gcd(-12, 18) == 6

def test_gcd_zero_cases():
    assert gcd(0, 5) == 5
    assert gcd(7, 0) == 7

def test_gcd_type_error():
    with pytest.raises(TypeError):
        gcd("8", 4)

# --- lcm ---
def test_lcm_happy_basic():
    assert lcm(4, 6) == 12

def test_lcm_happy_with_negatives():
    assert lcm(-3, 5) == 15

def test_lcm_zero():
    assert lcm(0, 10) == 0
    assert lcm(7, 0) == 0

def test_lcm_type_error():
    with pytest.raises(TypeError):
        lcm(3.5, 2)
