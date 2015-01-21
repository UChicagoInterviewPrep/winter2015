'''
Write a function which takes a pair of numbers and returns the quotient of the first by the second,
and the remainder when dividing the first by the second. You can't use any built-in division or modulus
functions of whatever language you use
'''
# naive solution O(n) in the dividen
def naive_divide(dividend, divisor):
    i = 0
    while (dividend > 0):
        dividend -= divisor
        i += 1
    return (i, dividend)

# optimized version: O(log2(n)) in the dividend
def optim_divide(dividend, divisor):
    i = 0
    j = 0
    remainder = dividend
    while dividend - divisor * 2**i > 0:
        i += 1
    i -= 1
    while i >= 0:
        remainder -= divisor * 2**i
        if remainder > 0:
            remainder += divisor * 2**i
        else:
            j += 2**i
    return (j, remainder)
