class primes:

    def __init__(self):
        self.next = 2

    def __iter__(self):
        return self

    def _is_prime(self, n):
        """基本思路：除以小于等于自身的平方根的所有正数都不能整除，且大于1"""
        if n < 2:
            return False

        if n in (2, 3):
            return True

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True

    def __next__(self):
        n = self.next
        while not self._is_prime(n):
            n += 1

        self.next = n + 1
        return n

if __name__ == '__main__':
    from itertools import islice
    from datetime import datetime
    t1 = datetime.now()
    lst = list(islice(primes(), 0, 100000))
    t2 = datetime.now()
    print(f'Found {len(lst)} primes in {t2 - t1}')