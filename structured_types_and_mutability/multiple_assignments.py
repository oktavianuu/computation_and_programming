# consider this
t1 = (1, 2, 3)
a, b, c = t1 # this will extract the the element in t1 individually and bind a to 1, b to 2, and c to 3.

# let's consider the functions that returns multiple values
def find_extreme_divisors(n1, n2):
    """
    Assumes that n1 and n2 are positive ints Returns a tuple containing the smallest common
    divisor > 1 and the largest common divisor of n1 & n2. If no common divisor, other than 1, returns (None, None)"""
    min_val, max_val = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            min_val = i
        max_val = i 
    return min_val, max_val

result = min_divisor, max_divisor = find_extreme_divisors(100, 200)
print(result)