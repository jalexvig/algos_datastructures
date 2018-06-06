

def rabin_karp(pattern, text):
    """
    Search for pattern in string.

    :param pattern: Needle.
    :param text: Haystack.
    :return: List of starting indices of pattern in text.
    """

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
    """
    Calculate an initial rolling hash.

    Rolling hashes are useful because they can be modified in O(1).

    :param s: String to compute rolling hash on.
    :param base: Used to shift current hash.
    :param prime: Prime number used to reduce size of hash.
    :return: Hash of string.
    """

    return sum(ord(c) * base ** i for i, c in enumerate(reversed(s))) % prime


def rolling_hash_optim(s, base, prime):
    """
    Calculate an initial rolling hash using prime to keep intermediate hash representations low.

    Rolling hashes are useful because they can be modified in O(1). Keeping intermediate hash representations low can
    prevent overflows.

    :param s: String to compute rolling hash on.
    :param base: Used to shift current hash.
    :param prime: Prime number used to reduce size of hash.
    :return: Hash of string.
    """

    res = 0

    for c in s[:-1]:
        res += ord(c)
        res %= prime
        res *= base

    res += ord(s[-1])
    res %= prime

    return res


def update_hash(n_pattern, base, prime):
    """
    Generate function to modify current hash.

    :param n_pattern: Number of characters in the pattern.
    :param base: Used to shift current hash.
    :param prime: Prime number used to reduce size of hash.
    :return: function.
    """

    diff = base ** (n_pattern - 1)

    def inner(c_old, c_new, h):
        """
        Update current hash.

        :param c_old: Character whose representation is being dropped from hash.
        :param c_new: Character whose representation is being added to hash.
        :param h: Current hash.
        :return: New hash.
        """

        h -= ord(c_old) * diff
        h *= base
        h += ord(c_new)
        h %= prime

        return h

    return inner


def update_hash_optim(n_pattern, base, prime):
    """
    Generate function to modify current hash.

    :param n_pattern: Number of characters in the pattern.
    :param base: Used to shift current hash.
    :param prime: Prime number used to reduce size of hash.
    :return: function.
    """

    diff = 1
    for i in range(n_pattern - 1):
        diff *= base
        diff %= prime

    def inner(c_old, c_new, h):
        """
        Update current hash using prime to keep intermediate hash represe

        Keeping intermediate hash representations low can prevent overflows.

        :param c_old: Character whose representation is being dropped from hash.
        :param c_new: Character whose representation is being added to hash.
        :param h: Current hash.
        :return: New hash.
        """

        res = ((h + prime - ord(c_old) * diff % prime) * base + ord(c_new)) % prime

        return res

    return inner


def rabin_karp_rolling(pattern, text, base=256, prime=101, optim=True):
    """
    Search for pattern in string using a rolling hash.

    :param pattern: Needle.
    :param text: Haystack.
    :param base: Used to shift current hash.
    :param prime: Prime number used to reduce size of hash.
    :param optim: Keep intermediate values low when computing/updating hash (can prevent overflows).
    :return: List of starting indices of pattern in text.
    """

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
