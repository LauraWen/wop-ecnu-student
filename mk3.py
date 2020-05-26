def is_prime(n):
    if n < 2:
        return False
    if n in (2,3):
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primes():
    n = 1
    while True:
        if is_prime(n):
            yield n
        n += 1

if __name__ == '__main__':
    from itertools import islice
    from datetime import datetime
    t1 = datetime.now()
    lst = list(islice(primes(), 0, 100000))
    t2 = datetime.now()
    print(f'Found {len(lst)} primes in {t2 - t1}')