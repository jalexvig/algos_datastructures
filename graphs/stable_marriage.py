"""
Marry individuals.

Summary:

    In a bipartite graph (each side equally sized) there are preferences between each node on one side and each node on
    the other side. Figure out pairings such that no two people should want to trade up upon meeting each other.

    1. Unengaged suitors pursue most sought after reviewer
    2. Reviewers choose their best suitor (or stay with current suitor)

    Repeat this until all parties are engaged. This is optimal for suitors (not necessarily reviewers).

Characteristics:

    * n number

    Worst Time: O(n ** 2)
"""

from collections import defaultdict


def stable_marriage(preferences_suitor: dict,
                    preferences_reviewer: dict):

    proposals = {}
    engaged_suitors = set()
    engagements = defaultdict(lambda: (None, -float('inf')))

    while len(engagements) != len(preferences_suitor):

        for suitor, prefs in preferences_suitor.items():
            if suitor in engaged_suitors:
                continue
            most_desired = prefs.pop()
            proposals.setdefault(most_desired[0], set()).add(suitor)

        for reviewer, suitors in proposals.items():
            suitor_current, score_current = engagements[reviewer]
            for s, score in reversed(preferences_reviewer[reviewer]):
                if score <= score_current:
                    break
                if s in suitors:
                    engagements[reviewer] = (s, score)
                    if suitor_current:
                        engaged_suitors.remove(suitor_current)
                    engaged_suitors.add(s)
                    break

    return engagements


if __name__ == '__main__':

    import random
    random.seed(1)

    n = 3
    prefs = list(range(n))

    preferences_suitor = {}
    for i in range(n):
        random.shuffle(prefs)
        p = zip(['x{}'.format(j) for j in range(n)], prefs)
        preferences_suitor['y{}'.format(i)] = sorted(p, key=lambda tup: tup[1])

    preferences_reviewer = {}
    for i in range(n):
        random.shuffle(prefs)
        p = zip(['y{}'.format(j) for j in range(n)], prefs)
        preferences_reviewer['x{}'.format(i)] = sorted(p, key=lambda tup: tup[1])

    print(stable_marriage(preferences_suitor, preferences_reviewer))
