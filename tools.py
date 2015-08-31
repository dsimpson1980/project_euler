# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def gen_primes(n=0):
    if n == 0:
        return esieve()
    else:
        gen = esieve()
        primes = [gen.next()]
        while primes[-1] < n:
            primes.append(gen.next())
        return primes


def esieve():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


def prime_factors(x):
    if x == 1:
        return {1: 1}
    factors, d = {}, 2
    while d <= x:
        if x % d == 0:
            x /= d
            factors[d] = factors.get(d, 0) + 1
        else:
            d += 1
    return factors

def divisor_generator(n):
    factors = prime_factors(n)
    factors = [(k, v) for k, v in factors.iteritems()]
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x]
                                        for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

class unique_element:
    def __init__(self, value, count):
        self.value = value
        self.count = count

def permutations(list_unique, result_list, d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in list_unique:
            if i.count > 0:
                result_list[d] = i._value
                i.count -= 1
                for g in permutations(list_unique, result_list, d - 1):
                    yield g
                i.count += 1

def unique_permutations(A):
    set_elements = set(A)
    list_unique = [unique_element(i, A.count(i)) for i in set_elements]
    u = len(A)
    return list(permutations(list_unique, [0] * u, u - 1))

def is_pandigital(n):
    a = sorted(str(n))
    for i in range(1, 10):
        if a[i - 1] != str(i):
            return False
    return True