"""
Search for a pattern in text.

Summary:

    1. Hash the pattern.
    2. For each substring of text that has length pattern, hash it and compare the hash to the hashed pattern.
    3. If the hash matches, confirm by checking the characters.

    This is improved by using a rolling hash. Rolling hashes are useful because they can be modified in O(1) time.

    1. Hash each element of the pattern.
    2. Shift each hash by increasing multiples of a base such that no information is lost when summed.
    3. Sum.
    4. Can mod this result to get it into a reasonable range.
    5. Repeat this process for the first correct-length substring of text.
    6. Do normal hash comparison followed by text comparison.
    7. Update the text hash by adding in the hash of the next character and subtracting the hash of the first (shifted
       by a multiple of the base).

Characteristics:

    * `m` = length of pattern
    * `n` = length of search text

    Worst Time: O(m n)
"""


def rabin_karp(pattern: str, text: str):

    res = []

    h = hash(pattern)

    for i in range(len(text) - len(pattern) + 1):

        substr = text[i: i + len(pattern)]

        if hash(substr) == h:
            for c1, c2 in zip(pattern, substr):
                if c1 != c2:
                    break
            else:
                res.append(i)

    return res


def rolling_hash(s: str, base: int, prime: int):

    return sum(ord(c) * base ** i for i, c in enumerate(reversed(s))) % prime


def rolling_hash_optim(s: str, base: int, prime: int):

    # Use the prime to keep intermediate hash values small

    res = 0

    for c in s[:-1]:
        res += ord(c)
        res %= prime
        res *= base

    res += ord(s[-1])
    res %= prime

    return res


def update_hash(n_pattern: int, base: int, prime: int):
    """Generate function to modify current hash."""

    diff = base ** (n_pattern - 1)

    def inner(c_old: str, c_new: str, h: int):
        """Update current hash."""

        h -= ord(c_old) * diff
        h *= base
        h += ord(c_new)
        h %= prime

        return h

    return inner


def update_hash_optim(n_pattern: int, base: int, prime: int):
    """Generate function to modify current hash."""

    # Use the prime to keep intermediate hash values small

    diff = 1
    for i in range(n_pattern - 1):
        diff *= base
        diff %= prime

    def inner(c_old: str, c_new: str, h: int):
        """Update current hash."""

        res = ((h + prime - ord(c_old) * diff % prime) * base + ord(c_new)) % prime

        return res

    return inner


def rabin_karp_rolling(pattern: str, text: str, base: int = 256, prime: int = 101, optim: bool = True):
    """Search for pattern in string using a rolling hash."""

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

    print(rabin_karp(pattern, text))
    print(rabin_karp_rolling(pattern, text, optim=True))
    print(rabin_karp_rolling(pattern, text, optim=False))
