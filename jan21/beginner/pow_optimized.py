import sys

# wrapper function to kick off work function
def pow_wrap(base, power):
    # handling incorrect cases
    assert power >= 0
    return pow_work(base, power, current)    

def pow_work(base, power, current):
    if power == 0:
        return current
    if power % 2 == 0:
        return pow_work(base * base, power / 2, current)
    else:
        return pow_work(base, power - 1, current * base)
    
def main():
    print('Please enter in the base number: ')
    base = int(sys.stdin.readline())
    
    print('Please enter in the power: ')
    power = int(sys.stdin.readline())
    
    print('The result of ', base, '^', power, ' is ', pow(base, power))

if __name__ == '__main__':
    main()
