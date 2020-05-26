def primes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p+q, []).append(p)
            del D[q]
        q += 1

if __name__ == '__main__':
    from itertools import islice
    from datetime import datetime
    t1 = datetime.now()
    lst = list(islice(primes(), 0, 100000))
    t2 = datetime.now()
    print(f'Found {len(lst)} primes in {t2 - t1}')