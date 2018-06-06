# Aho-Corasick

Search for patterns in a string.

1. Construct a [trie](https://en.wikipedia.org/wiki/Trie) of the patterns.
2. Recursively determine fail states by looking at parent's fail state.
3. Use trie to create DFA with non-matches following to fail states.

### Characteristics

* `m` = length of all patterns -- O(m) incurred when building the trie
* `n` = length of search string
* `z` = number matches

**Worst speed** : `O(m + n + z)`

### See also

* This is [KMP](https://github.com/jalexvig/learn_algos/tree/master/string_search/kmp) extended to multiple patterns
