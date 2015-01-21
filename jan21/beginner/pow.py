import sys

def pow(base, power):
    if power <= 0:
        return 1
    else:
        return base * pow(base, power-1)

def main():
    print('Please enter in the base number: ')
    base = int(sys.stdin.readline())
    
    print('Please enter in the power: ')
    power = int(sys.stdin.readline())
    
    print('The result of ', base, '^', power, ' is ', pow(base, power))

if __name__ == '__main__':
    main()
