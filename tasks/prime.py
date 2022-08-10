__all__ = (
    'is_prime',
)
from math import trunc

def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    i = 2
    if(number == 0 or number == 1):
        return False
    while(i<= number**(1/2)):
        if(number % i == 0):
            return False
        i += 1
    return True
