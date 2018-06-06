

def naive(pattern, text):
    """
    Naive pattern matching

    Args:
        pattern: pattern to search for
        text:  text to search in

    Returns: list of indices of matches
    """

    res = []
    n = len(text)

    for i in range(n):
        for j, c in enumerate(pattern):
            if i + j == n or text[i + j] != c:
                break
        else:
            res.append(i)

    return res


def kmp(pattern, text):
    """
    KMP

    Args:
        pattern: pattern to search for
        text:  text to search in

    Returns: list of indices of matches
    """

    # DFA with n+1 states
    # when reach last state we have a match
    # first state is 0 characters matching

    res = []

    fail_jumps = construct_fail_jumps(pattern)

    # state of dfa (maximal number characters matched)
    len_substr = 0

    for j, c in enumerate(text):

        # move dfa back to longest match
        while len_substr > 0 and c != pattern[len_substr]:
            len_substr = fail_jumps[len_substr-1]

        if c == pattern[len_substr]:
            # increment dfa state
            len_substr += 1

            if len_substr == len(pattern):
                # dfa in match state
                res.append(j - len_substr + 1)
                len_substr = fail_jumps[-1]

    return res


def construct_fail_jumps(pattern):
    """
    Get lengths of longest proper prefixes that are suffixes at every position.

    Args:
        pattern: pattern to analyze

    Returns: list
    """

    longest_substr = [0]

    for i in range(1, len(pattern)):

        len_substr = longest_substr[-1]

        while len_substr > 0 and pattern[len_substr] != pattern[i]:
            len_substr = longest_substr[len_substr-1]

        longest_substr.append(len_substr + (pattern[len_substr] == pattern[i]))

    return longest_substr


if __name__ == '__main__':

    import random
    import string
    import time

    alphabet = string.ascii_lowercase[:4]

    text = ''.join(random.choice(alphabet) for _ in range(10 ** 6))
    pat = ''.join(random.choice(alphabet) for _ in range(5))

    print('data generated')

    t0 = time.time()
    res_naive = naive(pat, text)
    t_naive = time.time() - t0

    t0 = time.time()
    res_kmp = kmp(pat, text)
    t_kmp = time.time() - t0

    print(t_naive, t_kmp, res_naive == res_kmp, len(res_naive))
