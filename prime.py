import math

# Returns True or False based on wether the given value is Prime or not
def isPrime(n:int):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n%2 == 0:
        return False
    else:
        root = int(math.sqrt(n)) + 1
        for i in range(3, root, 2):
            if n % i == 0:
                return False
    return True

# Returns a list of all the primes in a specified range of numbers
def rangePrime(first:int, last:int):
    primeNums = []

    for x in range(first, last):
        if isPrime(x):
            primeNums.append(x)
        continue

    return primeNums

# Returns the next consecutive prime number after the given number
def next(n:int):
    i = n

    if isPrime(i):
        i = i + 1

    while isPrime(i) == False:
        if isPrime(i + 1) == True:
            return(i + 1)
        else:
            i = i + 1

# Returns the previous consecutive prime number before the given number
# example: n = 10 --> the closest previous prime number is 7
def previous(n:int):
    i = n

    if isPrime(i):
        i = i - 1

    while isPrime(i) == False:
        if isPrime(i - 1) == True:
            return(i - 1)
        else:
            i = i - 1

# Sums all the prime numbers up to a given range
def rangeSum(n:int):
    primeNums = []
    
    for x in range(n):
        if isPrime(x):
            primeNums.append(x)
        continue

    total = 0

    for x in range(len(primeNums)):
        total = total + primeNums[x]

    return total

# Returnes the value of the nth (given) prime number
# for example inputting 5 would return the 5th prime number
def primeNumber(n:int):
    targetNumber = 0

    for x in range(n):
        targetNumber = targetNumber + 1
        while not isPrime(targetNumber):
            targetNumber = targetNumber + 1

    return targetNumber

# Returns a list of consecutive prime numbers from the nth prime
# to the mth prime (inclusive).
# Example: primeNumbers(3, 5) returns [5, 7, 11]
# So it will return prime numbers from the 3rd prime number to the 5th prime number
def primeNumbers(first:int, last:int):
    li = []
    for x in range(first, last + 1):
        li.append(primeNumber(x))
    return li

# Returns true if n is a Mersenne Prime
def isMersennePrime(n:int):
    return isPrime((2 ** n) - 1)


# Returns a list of all the prime factors of n
# if indicies is True, it will return a dictionary
# with each prime factor as the key (int) and the 
# indicie which corresponds (value)
def factors(number: int, indicies: bool):
    match number:
        case 1: return [1]
        case 0: return "invalid number"
        case x if x < 0:
            number = number * (-1)
        case x if x % 1 != 0: return "invalid number"

    primeFactors = []
    if isPrime(number):
        primeFactors.append(1)
        primeFactors.append(number)
        if not indicies:
            return primeFactors
    
    i = number
    primeList = rangePrime(0, number//2)

    while not isPrime(i):
        for x in primeList:
            if i % x == 0:
                i = i // x
                primeFactors.append(x)
                if isPrime(i):
                    primeFactors.append(i)
                break
            else:
                continue

    if indicies:
        powers = {}
        powers[primeFactors[0]] = 1

        for x in range(1, len(primeFactors)):
            if primeFactors[x] == primeFactors[x - 1]:
                powers[primeFactors[x]] += 1
            else:
                powers[primeFactors[x]] = 1

        return powers

    return primeFactors 


# Returns the position of the inputed prime number
def index(n:int):
    if not isPrime(n):
        return "Not a prime number"
    else:
        position = 0
        primeList = rangePrime(0, n + 1)
        for i in range(len(primeList)):
            position = position + 1
    return position
