def zeros(n):
    """
    Recursive method to calculate the number of trailing zeros in a factorial of a given number n.
    
    Recall that number of trailing zeros is equivalent to the highest power of ten that divides the number without remainder.

    Use known base values and the fact that each increase of n by 1 only adds new factors, so will never decrease the number of trailing zeros. It will increase according to how many new factors of 10 are introduced. 
    
    Note that due to the plentiful availability of factors of 2, we can restrict to looking for factors of 5 instead.
    """
    if n == 0 or n == 1:
        return 0
    num_of_fives = 0
    test = n
    while True:
        if test % 5 != 0:
            break
        num_of_fives += 1
        test //= 5
    return zeros(n - 1) + num_of_fives


def zeros_2(n):
    """
    Alternative, faster method which directly uses the fact that we can count new factors of 10 introduced in the factorial multiplication by counting the factors which are divisible by a power of 5 (due to the plentiful supply of factors of 2).
    
    Thus, a factor divisible by 5 ** k introduces k new factors of 10.
    """
    max_power_of_5 = 0
    while True:
        if n / (5 ** (max_power_of_5 + 1)) < 1:
            break
        max_power_of_5 += 1
    return sum([n // (5 ** k) for k in range(1, max_power_of_5 + 1)])


print(zeros_2(6))