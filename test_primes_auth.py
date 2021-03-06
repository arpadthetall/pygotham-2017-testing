"""
Defines unit tests for the "primes" module, with authentication.
"""

import pytest

from primes_auth import is_prime, prime_factors, User


def test_is_prime():
    user = User('python', 'rocks')
    assert is_prime(user, 2) is True
    assert is_prime(user, 3) is True
    assert is_prime(user, 4) is False


def test_prime_factors():
    user = User('python', 'rocks')
    assert prime_factors(user, 2) == [2]
    assert prime_factors(user, 12) == [2, 2, 3]


def test_pytest_raises():
    user = User('python', 'bogus')
    with pytest.raises(RuntimeError):
        prime_factors(user, 2)

    # Equivalent to:
    try:
        prime_factors(user, 2)
        raise Exception('Failed to raise RuntimeError')
    except RuntimeError:
        pass
