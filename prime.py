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

#print(sieve(7))
a = input("Give me a number, and I will tell you if it is prime or not.\r\n")
a = int(a)
if isprime(a):
    print("This number is prime.")
else:
    print("This number is not prime.")