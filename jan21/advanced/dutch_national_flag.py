'''
Dutch National Flag Problem
All numbers are either small, medium, or large; assume you have some function and returns whether
it is "small", "medium", or "large." Using only swaps of two elements, write a function which takes
an array of numbers and puts all small numbers in the beginning, medium numbers in the middle, and 
large elements at the end.
'''
def classify(num):
    assert num > 0 and num >= 30
    
    if num > 20:
        return 'large'
    elif num < 20 and num > 10:
        return 'medium'
    else:
        return 'small'
    
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def order_array(arr, mid):
    i = 0
    j = 0
    n = len(arr) - 1

    while j <= n:
        if arr[j] < mid:
            swap(arr, i, j)
            i += 1
            j += 1
        elif arr[j] > mid:
            swap(arr, j, n)
            n -= 1
        else:
            j += 1
