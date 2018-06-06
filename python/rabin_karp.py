

def rabin_karp(pattern, text):

    # hash pattern
    # compare substrings of text to the hash of the pattern

    res = []

    h = hash(pattern)

    for i in range(len(text) - len(pattern)):

        substr = text[i: i + len(pattern)]

        if hash(substr) == h:
            for c1, c2 in zip(pattern, substr):
                if c1 != c2:
                    break
            else:
                res.append(i)

    return res


def rolling_hash(s, base, prime):

    return sum(ord(c) * base ** i for i, c in enumerate(reversed(s))) % prime


def rolling_hash_optim(s, base, prime):

    res = 0

    for c in s[:-1]:
        res += ord(c)
        res %= prime
        res *= base

    res += ord(s[-1])
    res %= prime

    return res


def update_hash(n_pattern, base, prime):

    diff = base ** (n_pattern - 1)

    def inner(c_old, c_new, h):

        h -= ord(c_old) * diff
        h *= base
        h += ord(c_new)
        h %= prime

        return h

    return inner


def update_hash_optim(n_pattern, base, prime):

    diff = 1
    for i in range(n_pattern - 1):
        diff *= base
        diff %= prime

    def inner(c_old, c_new, h):

        res = ((h + prime - ord(c_old) * diff % prime) * base + ord(c_new)) % prime

        return res

    return inner


def rabin_karp_rolling(pattern, text, base=256, prime=101, optim=True):

    res = []
    n = len(pattern)

    if optim:
        rolling_hash_fn = rolling_hash_optim
        update_hash_closure = update_hash_optim
    else:
        rolling_hash_fn = rolling_hash
        update_hash_closure = update_hash

    update_hash_fn = update_hash_closure(n, base, prime)

    h_pattern = rolling_hash_fn(pattern, base, prime)
    h_substr = rolling_hash_fn(text[:n], base, prime)

    for i in range(len(text) - n + 1):

        if h_pattern == h_substr and pattern == text[i: i + n]:
            res.append(i)

        if i + n < len(text):
            h_substr = update_hash_fn(text[i], text[i + n], h_substr)

    return res


if __name__ == '__main__':

    pattern = 'ab'
    text = 'cabab'

    print(rabin_karp_rolling(pattern, text, optim=True))
    print(rabin_karp_rolling(pattern, text, optim=False))
