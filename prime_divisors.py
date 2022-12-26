def sieve(x):
    primes = []
    l = [*range(2, x + 1)]
    while len(l) > 0:
        for i in l:
            if i != l[0] and i % l[0] == 0:
                l.remove(i)
        primes.append(l.pop(0))

    return primes

def isprime(y):
    z = sieve(y)
    return y in z
    

def multiples(a):
    divisors = []
    b = int(a / 2)
    c = b + 1
    for h in range(c):
        if h != 0 and a % h == 0:
            divisors.append(h)
    divisors.append(a)
    return(divisors)

a = input("Give me a number, and I will tell you if it is prime or not.\r\n")
a = int(a)

if isprime(a):
    print("This number is prime. Its divisors are only", multiples(a))
else:
    print("This number is not prime. Its divisors are", multiples(a))